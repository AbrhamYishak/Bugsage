class BugsageError(Exception):
    pass

class InvalidAPIKeyError(BugsageError):
    pass

class NoInternetError(BugsageError):
    pass

class RateLimitError(BugsageError):
    pass

class NextPageError(BugsageError):
    pass

class PrevPageError(BugsageError):
    pass