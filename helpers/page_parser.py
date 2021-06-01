import requests
from bs4 import BeautifulSoup, element

from helpers.page import Page
import helpers.config as config
from helpers.listing import Listing

def get_page_data(URL: str, page_config: Page):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    info = soup.find_all(page_config.info_attributes_bs4_block, class_=page_config.info_attributes_bs4_class, attrs=page_config.info_attributes_bs4_attrs)[0]
    summary = soup.find_all(page_config.summary_attributes_bs4_block, class_=page_config.summary_attributes_bs4_class, attrs=page_config.summary_attributes_bs4_attrs)[0]
    
    if info != None:
        info = info.text.strip()
        summary = summary.text.strip()
        return (info, summary)
    
    return ('','')

def get_listing_entry(ad: element.Tag, reviewed_listings: dict, page_config: Page) -> (Listing, bool):
    href = ad.find_all(page_config.href_parser, href=True)[0]['href']
    URL = href if page_config.default_url == "" else page_config.default_url + href

    if URL in reviewed_listings:
        return None, False

    info, summary = get_page_data(URL, page_config)
    listing = Listing(page_url=URL,
                      summary=summary,
                      info=info)
    reviewed_listings[URL] = ''

    return listing, True