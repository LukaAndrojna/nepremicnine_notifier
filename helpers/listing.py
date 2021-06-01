class Listing:
    def __init__(self, page_url: str, summary: str, info: str):
        self._page_url = page_url
        self._summary = summary
        self._info = info
    
    def report(self) -> str:
        return f'{self._page_url}\n{self._info}\n{self._summary}\n'
