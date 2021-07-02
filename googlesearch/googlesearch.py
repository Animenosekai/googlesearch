"""
googlesearch v1.1.1 (Stable)

© Anime no Sekai — 2021
"""
from urllib.parse import quote

from requests import get
from bs4 import BeautifulSoup
from pyuseragents import random

from googlesearch.utils.cleanup import remove_all
from googlesearch.models import SearchResultElement
from googlesearch.exceptions import CleanupError, InvalidParameter, ParsingError, RelatedSearchError, RequestError, ResultsError, GoogleSearchException
from googlesearch.constants import BASE_URL, CONSENT_VALUE, CLEANUP_TAGS, HEADERS

class Search():
    def __init__(self, query: str, language: str = "en", number_of_results: int = 10, retry_count: int = 3, parser: str = "html.parser") -> None:
        self.query = str(query)
        self.retry_count = int(retry_count)
        if self.retry_count < 1:
            raise InvalidParameter("'retry_count' cannot be less than 1")
        self.loaded = False
        
        # parameters
        self._query = quote(self.query, safe='')
        self._language = quote(language, safe='')
        if number_of_results < 1:
            raise InvalidParameter("'number_of_results' cannot be less than 1")
        self._requested_number_of_results = int(number_of_results)
        self._headers = HEADERS.copy()
        self._headers["User-Agent"] = random()
        self._parser = str(parser)
        
        # storing values, can be accessed without loading
        self._related_searches = []
        self._results = []

    def _check_loading_state(self):
        # def decorator(function):
        #     return function()
        if not self.loaded:
            for i in range(1, self.retry_count + 1):
                try:
                    self.load()
                    break
                except GoogleSearchException as e:
                    if i >= self.retry_count:
                        raise e
                    continue
            
        # return decorator

    def load(self):
        try:
            response = get(BASE_URL.format(query=self._query, language=self._language, number=str((int(self._requested_number_of_results) - 1 if self._requested_number_of_results >= 2 else 1))), headers=self._headers, cookies={"CONSENT": CONSENT_VALUE})
            if response.status_code >= 400:
                raise RequestError("Google Returned Status Code: " + str(response.status_code))
        except:
            RequestError("An error occured while requesting for the webpage to parse")
        
        try:
            # parse the response
            website = BeautifulSoup(response.text, features=self._parser)

            # cleanup
            try:
                for tag in CLEANUP_TAGS:
                    remove_all(website, tag)
            except Exception as e:
                raise CleanupError("An error occured while cleaning up the retrieved webpage (error: {err})".format(err=str(e)))

            # retrieving
            try:
                _related_history = []
                for associate in website.find("div", {"id": "main"}).find_all("div", recursive=False)[-1].find("div").find_all("div"):
                    if len(associate.find_all("a")) >= 1:
                        _related_history.append(associate.text)
                for element in set(_related_history):
                    self._related_searches.append(Search(element, parser=self._parser, retry_count=self.retry_count))
            except Exception as e:
                if self._requested_number_of_results > 95:
                    extra_error = " This error might come from the high number of results asked for. "
                else:
                    extra_error = ""
                raise RelatedSearchError("An error occured while parsing the related searches.{extra}(error: {err})".format(extra=extra_error, err=str(e)))

            try:
                for result in website.select("#main > div > div"):
                    try:
                        self._results.append(SearchResultElement(result))
                    except Exception:
                        continue
            except Exception as e:
                raise ResultsError("An error occured while parsing the results (error: {err})").format(err=str(e))
            
            self.loaded = True
            self._response = str(website)
        except GoogleSearchException as e:
            raise e
        except Exception as e:
            raise ParsingError("An error occured while parsing Google Search results (error: {err})").format(err=str(e))

    # properties declaration

    @property
    def related_searches(self):
        self._check_loading_state()
        return self._related_searches

    @related_searches.setter
    def related_searches(self, value):
        self._related_searches = value

    @property
    def results(self):
        self._check_loading_state()
        return self._results

    @results.setter
    def results(self, value):
        self._results = value
    
    # class functions
    def __repr__(self) -> str:
        return '<Search query="{query}" results={results_count}>'.format(query=self.query, results_count=(str(len(self.results)) + " elements" if self.loaded else "(Not loaded)"))

    def as_dict(self) -> str:
        return {
            "query": self.query,
            "language": self._language,
            "requestedNumberOfResults": self._requested_number_of_results,
            "results": [elem.as_dict() for elem in self.results],
            "relatedSearches": [elem.query for elem in self.related_searches]
        }