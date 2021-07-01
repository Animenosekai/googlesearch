"""
File containing the different exceptions which can be raised in googlesearch
"""

class GoogleSearchException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class InvalidParameter(GoogleSearchException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class RequestError(GoogleSearchException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ParsingError(GoogleSearchException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class CleanupError(ParsingError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class RelatedSearchError(ParsingError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ResultsError(ParsingError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)