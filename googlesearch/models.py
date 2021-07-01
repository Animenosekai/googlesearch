"""
File containing the different classes used in googlesearch
"""

from urllib.parse import urlparse, parse_qsl
from bs4 import BeautifulSoup
from googlesearch.constants import BASE

class SearchResultElement():
    def __init__(self, resultobj: BeautifulSoup) -> None:
        # get the url
        href = str(resultobj.find("a")["href"])
        if href.startswith("/"):
            href = BASE + href
        self.url = str(dict(parse_qsl(urlparse(href).query))["q"])

        # get the title
        self.title = str(resultobj.find("h3").text)
        self.displayed_url = str(resultobj.select_one("div:nth-child(1) > a > div").text)
        self.description = str(resultobj.find_all("div")[-1].text)

    def __repr__(self) -> str:
        return '<SearchResult title="{title}" ({url})>'.format(title=self.title, url=self.displayed_url)

    def as_dict(self) -> str:
        return {
            "url": self.url,
            "title": self.title,
            "displayedURL": self.displayed_url,
            "description": self.description
        }