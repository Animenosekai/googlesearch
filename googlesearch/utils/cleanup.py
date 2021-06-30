from bs4 import BeautifulSoup

def remove_all(bsobject: BeautifulSoup, tag: str):
    """
    Removes all of the elements with the given tag recursively
    """
    for element in bsobject.find_all(tag):
        element.decompose()
