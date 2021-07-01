"""
Constants.py

Stores the constants for the Python Google Search module
"""
# request
BASE = "https://www.google.com"
BASE_URL = BASE + "/search?client=safari&rls=en&gbv=1&q={query}&hl={language}&num={number}"
CONSENT_VALUE = "YES+cb"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Host": "www.google.com",
    "Accept-Language": "en-us"
}

# parser
# BEAUTIFULSOUP_PARSER = "html.parser"
CLEANUP_TAGS = ["script", "style", "svg", "header", "textarea"]