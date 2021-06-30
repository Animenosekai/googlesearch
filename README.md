# `googlesearch`

> `googlesearch` lets you use Google Searching capabilities right from your Python code or from your CLI

***Make any Google Search right from Python!***

[![PyPI version](https://badge.fury.io/py/googlesearch.svg)](https://pypi.org/project/googlesearch/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/googlesearch)](https://pypistats.org/packages/googlesearch)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/googlesearch)](https://pypi.org/project/googlesearch/)
[![PyPI - Status](https://img.shields.io/pypi/status/googlesearch)](https://pypi.org/project/googlesearch/)
[![GitHub - License](https://img.shields.io/github/license/Animenosekai/googlesearch)](https://github.com/Animenosekai/googlesearch/blob/master/LICENSE)
[![GitHub top language](https://img.shields.io/github/languages/top/Animenosekai/googlesearch)](https://github.com/Animenosekai/googlesearch)
[![CodeQL Checks Badge](https://github.com/Animenosekai/googlesearch/workflows/CodeQL%20Python%20Analysis/badge.svg)](https://github.com/Animenosekai/googlesearch/actions?query=workflow%3ACodeQL)
[![Pytest](https://github.com/Animenosekai/googlesearch/actions/workflows/pytest.yml/badge.svg)](https://github.com/Animenosekai/googlesearch/actions/workflows/pytest.yml)
![Code Size](https://img.shields.io/github/languages/code-size/Animenosekai/googlesearch)
![Repo Size](https://img.shields.io/github/repo-size/Animenosekai/googlesearch)
![Issues](https://img.shields.io/github/issues/Animenosekai/googlesearch)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need Python 3 to use this module

```bash
# vermin output
Minimum required versions: 3.2
Incompatible versions:     2
```

According to Vermin, Python 3.2 is needed

Always check if your Python version works with `googlesearch` before using it in production

## Installing

### Option 1: From PyPI

```bash
pip install googlesearch
```

### Option 2: From Git

```bash
pip install https://github.com/Animenosekai/googlesearch
```

You can check if you successfully installed it by printing out its version:

```bash
$ python -c "import googlesearch; print(googlesearch.__version__)"
# output:
googlesearch v1.0
```

<!--If a CLI version is available-->

or just:

```bash
$ googlesearch --version
# output:
googlesearch v1.0
```

## Usage

You can use googlesearch in Python by importing it in your script:

```python
>>> from googlesearch import Search
>>> python_results = Search("Python")
>>> python_results.results
[<SearchResult title="Python.org" (www.python.org)>, <SearchResult title="Python" ()>, <SearchResult title="Python (langage) — Wikipédia" (fr.wikipedia.org › wiki › Python_(langage))>, ...]
```

### CLI usage

You can use googlesearch in other apps by accessing it through the CLI version:

```bash
$ googlesearch --query Python
{
    "query": "Python",
    "results": [
        {
            "url": "https://www.python.org/",
            "title": "Welcome to Python.org",
            "displayedURL": "www.python.org",
            "description": "The official home of the Python Programming Language.\nDownloads \u00b7 Python For Beginners \u00b7 Quotes about Python \u00b7 Python Essays"
        },
        [...]
    ],
    "relatedSearches": [
        "Python serpent",
        "Python openclassroom",
        [...]
    ],
    "success": true
}
```

#### Interactive Shell (REPL)

An interactive version of the CLI is also available

```bash
$ googlesearch
Enter '.quit' to exit googlesearch
[?] (googlesearch ~ Query) > : ... # enter your query

[?] What do you want to do?: # select the result with your keyboard's arrows and [enter]

—————————————————SEARCH RESULT—————————————————
[...] # site's name

Description: # the site's description
URL: ... # site's URL
Related Searches: # a max of 3 related searches
```

### As a Python module

## Search

The search class represents a Google Search.

It lets you retrieve the different results/websites (`Search.results`) and the related searches (`Search.related_searches`)

### How to use

This class is lazy loading the results.

When you initialize it with `Search()`, it takes a `query` as the required parameter and the `parser` and `retry_count` as optional parameters.

It will only load and parse the website when `results` or `related_searches` is called.

`parser` is the `BeautifulSoup` parser used to parse the website and `retry_count` is a positive integer representing the number of retries done before raising an exception (useful as `googlesearch` seems to fail sometimes).

`results` is a list of `googlesearch.models.SearchResultElement`.

`related_searches` is a list of `Search` elements.

## SearchResultElement

This class represents a result and is initialized by `googlesearch`.

It holds the following information:

- `url`: The URL of the website
- `title`: The title of the website
- `displayed_url`: The URL displayed on Google Search
- `description`: The description of the website

### Extra

Every class has the `as_dict` function which converts the object into a dictionary. For `Search`, the as_dict function will convert the other `Search` objects in `related_search` to a string with the query.

## Deployment

This module is currently in development and might contain bugs.

Feel free to use it in production if you feel like it is suitable for your production even if you may encounter issues.

## Built With

- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) - To parse the HTML
- [requests](https://github.com/psf/requests) - To make HTTP requests
- [pyuseragents](https://github.com/Animenosekai/useragents) - To create the `User-Agent` HTTP header
- [inquirer](https://github.com/magmax/python-inquirer) - To make a beautiful CLI interface

## Authors

- **Anime no Sekai** - *Initial work* - [Animenosekai](https://github.com/Animenosekai)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more details
