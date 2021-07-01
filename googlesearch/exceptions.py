"""
File containing the different exceptions which can be raised in googlesearch
"""

class googlesearchException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class InvalidParameter(googlesearchException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class RequestError(googlesearchException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ParsingError(googlesearchException):
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