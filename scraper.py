from os import path
import json
import requests
from time import sleep
import concurrent.futures
from bs4 import BeautifulSoup

from helpers.listings import Listings
from helpers.page import Page
import helpers.email_notification as email_notification
import helpers.config as config

def main():
    page_config: Page
    for page_config in config.configuration:
        reviewed_listings = {}
        file_path = f'JSON/{page_config.key}.json'
        if not path.exists(file_path):
            with open(file_path, "w") as file:
                file.write("{}")
        
        with open(file_path) as json_file:
            reviewed_listings = json.load(json_file)

        listings = Listings(reviewed_listings)

        for i in range(1, 1000):
            page = requests.get(config.get_serach_url(page_config.page_url, i))
            soup = BeautifulSoup(page.content, 'html.parser')

            ads = soup.find_all(page_config.bs4_block, attrs=page_config.bs4_attrs)
            ads_len = len(ads)
            if ads_len == 0:
                break
            with concurrent.futures.ThreadPoolExecutor(max_workers=ads_len) as executor:
                for ad in ads:
                    executor.submit(listings.parse_listing, ad, page_config)
        
        email_msg = listings.generate_email()
        if email_msg != '':
            email_notification.send(page_config, email_msg)
        
        with open(file_path, 'w') as fp:
            json.dump(listings.get_reviewed_listings(), fp)

if __name__ == "__main__":
    main()
