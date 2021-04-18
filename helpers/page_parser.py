import requests
from bs4 import BeautifulSoup, element

import helpers.config as config


class Listing:
    def __init__(self, page_url: str, summary: str, info: str):
        self._page_url = page_url
        self._summary = summary
        self._info = info
    
    def report(self) -> str:
        return f'{self._page_url}\n{self._info}\n{self._summary}\n'
    

def get_page_data(URL: str):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    info = soup.find_all('div', class_='more_info')[0]
    summary = soup.find_all('div', class_='kratek')[0]
    if info != None:
        info = info.text.strip()
        summary = summary.text.strip()
        return (info, summary)
    
    return ('','')


def get_listing_entry(ad: element.Tag, reviewed_listings: dict) -> (Listing, bool):
    href = ad.find_all('a', href=True)[0]['href']
    URL = config.DEFAULT_URL + href

    if URL in reviewed_listings:
        return None, False

    info, summary = get_page_data(URL)
    listing = Listing(page_url=URL,
                      summary=summary,
                      info=info)
    reviewed_listings[URL] = ''

    return listing, True