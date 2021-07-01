"""
File containing the CLI version of googlesearch
"""

import argparse
import inquirer
import googlesearch
from urllib.parse import urlparse
from json import dumps

INPUT_PREFIX = "(\033[90mgooglesearch ~ \033[0m{action}) > "

def boolean_type(value):
    """
    Defaults to False
    """
    return value in {'yes', 'true', 't', 'y', '1'}
    
def main():
    parser = argparse.ArgumentParser(prog='googlesearch', description='This module lets you use Google Searching capabilities right from your code')

    parser.add_argument('--version', '-v', action='version', version=googlesearch.__version__)
    
    # optional
    parser.add_argument('--query', '-q', type=str, help='The string query to search on Google (If not specified, the interactive mode will be enabled)', required=False, default=None)
    parser.add_argument('--parser', '-p', type=str, help='The HTML parser to use (Default: html.parser)', required=False, default="html.parser")
    parser.add_argument('--minify', '-m', type=boolean_type, help='If the response in the non-interactive mode should be minified or not (Default: False)', required=False, default=False)
    parser.add_argument('--retry-count', '-r', type=int, help='The number of times the request should be retried before raising an exception (Default: 3)', required=False, default=3)
    
    args = parser.parse_args()

    if args.query is not None:
        try:
            result = googlesearch.Search(query=args.query, parser=args.parser, retry_count=args.retry_count).as_dict()
            result["success"] = True
        except googlesearch.exceptions.googlesearchException:
            result = {"success": False}
        if args.minify:
            print(dumps(result, separators=(",", ":")))
        else:
            print(dumps(result, indent=4))
    else:
        while True:
            print("\033[96mEnter '.quit' to exit googlesearch\033[0m")
            answers = inquirer.prompt([
                inquirer.Text(
                    name='query',
                    message=INPUT_PREFIX.format(action="Query")
                )
            ])
            if answers["query"] == ".quit":
                break
            result = googlesearch.Search(query=answers["query"], parser=args.parser, retry_count=args.retry_count)
            print("")
            try:
                answers = inquirer.prompt([
                    inquirer.List(
                        name='chosen',
                        message="What do you want to do?",
                        choices=[str(index) + " — " + result.title + " (" + urlparse(result.url).netloc + ")" for index, result in enumerate(result.results, start=1)] + ["Quit"],
                        carousel=True
                    )
                ])
            except googlesearch.exceptions.googlesearchException:
                print("\033[90mAn error occured while searching up \033[0m" + str(answers["query"]) + " \033[90mon Google\033[0m")
                continue
            if answers["chosen"] == "Quit":
                break
            chosen_index = ""
            for element in answers["chosen"]:
                element = str(element)
                if element.isdecimal():
                    chosen_index += element
            chosen_result = result.results[int(chosen_index) - 1]
            print("—————————————————SEARCH RESULT—————————————————")
            print("[" + chosen_result.title + "]")
            print("")
            print("\033[90mDescription:\033[0m", chosen_result.description)
            print("\033[90mURL:\033[0m", chosen_result.url)
            print("\033[90mRelated Searches:\033[0m", ", ".join([search.query for index, search in enumerate(result.related_searches) if index < 3]))
            print("")
            print("")