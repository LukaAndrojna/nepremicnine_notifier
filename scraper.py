import json
import requests
from os import path
import concurrent.futures
from bs4 import BeautifulSoup

from helpers.page import load_configs
from helpers.listings import Listings
from helpers.mail import Mail

def main():
    try:
        for page_config in load_configs():
            reviewed_listings = {}
            file_path = f'JSON/{page_config.key}.json'
            if not path.exists(file_path):
                with open(file_path, "w") as file:
                    file.write("{}")
            
            with open(file_path) as json_file:
                reviewed_listings = json.load(json_file)

            listings = Listings(reviewed_listings)
            for i in range(1, 1000):
                page = requests.get(page_config.get_serach_url(i))
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
                Mail().set_parameters_listings(page_config, email_msg).send()
            
            with open(file_path, 'w') as fp:
                json.dump(listings.get_reviewed_listings(), fp)
            
    except Exception as e:
        mail_body = 'Error occured while running script for nepremicnine scrapper. Check what is going on!\n' + str(e)
        Mail().set_parameters_error(
                page_config.from_email,
                page_config.gmail_api_key,
                page_config.admin_mail,
                "Nepremicnine scrapper error occured",
                mail_body).send()

if __name__ == "__main__":
    main()
