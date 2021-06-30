import pygooglesearch
from pygooglesearch import Search
from pygooglesearch.models import SearchResultElement

def test_search():
    print("[test] --> Testing Search")
    python = Search("Python")
    assert python.query == "Python"
    assert python._query == "Python"
    assert Search("How is the weather in Tokyo?")._query == "How%20is%20the%20weather%20in%20Tokyo%3F"
    assert python.loaded == False
    assert isinstance(python.results, list)
    assert isinstance(python.related_searches, list)
    assert python.loaded == True
    assert isinstance(python.results[0], SearchResultElement)
    assert isinstance(python.related_searches[0], Search)
    assert python.related_searches[0].loaded == False