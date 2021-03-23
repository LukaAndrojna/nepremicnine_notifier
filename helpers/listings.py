import threading

import config
import page_parser


class Listings:
    def __init__(self, reviewed_listings: dict):
        self._reviewed_listings = reviewed_listings
        self._listings_to_report = list()
        self._lock = threading.Lock()
    
    def parse_listing(self, ad):
        listing, success = page_parser.get_listing_entry(ad, self._reviewed_listings)
        with self._lock:
            if success:
                self._listings_to_report.append(listing)
    
    def generate_email(self) -> str:
        print(len(self._listings_to_report))
        return '\n'.join([listing.report() for listing in self._listings_to_report])

    def get_reviewed_listings(self) -> dict:
        return self._reviewed_listings