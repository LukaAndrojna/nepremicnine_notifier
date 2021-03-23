import json
import requests
from time import sleep
import concurrent.futures
from bs4 import BeautifulSoup

import helpers.config as config
from helpers.listings import Listings
import helpers.email_notification as email_notification



def main():
    reviewed_listings = {}
    with open(config.json_file) as json_file:
        reviewed_listings = json.load(json_file)

    listings = Listings(reviewed_listings)

    for i in range(1,1000):
        page = requests.get(config.get_serach_url(i))
        soup = BeautifulSoup(page.content, 'html.parser')

        ads = soup.find_all('div', attrs={'class':'oglas_container', 'itemtype': 'http://schema.org/ListItem'})
        ads_len = len(ads)
        if ads_len == 0:
            break
        with concurrent.futures.ThreadPoolExecutor(max_workers=ads_len) as executor:
            for ad in ads:
                executor.submit(listings.parse_listing, ad)

    email_msg = listings.generate_email()
    if email_msg != '':
        email_notification.send(email_msg)

    with open(config.json_file, 'w') as fp:
        json.dump(listings.get_reviewed_listings(), fp)



if __name__ == "__main__":
    main()
