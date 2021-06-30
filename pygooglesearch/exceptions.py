"""
File containing the different exceptions which can be raised in pygooglesearch
"""

class pygooglesearchException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class InvalidParameter(pygooglesearchException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class RequestError(pygooglesearchException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ParsingError(pygooglesearchException):
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