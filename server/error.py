from common.constants import ERRORS, MESSAGE
class ValidationException(Exception):
    def __init__(self, payload=None, status_code=None):
        Exception.__init__(self)
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = {}
        rv[ERRORS] = self.payload
        return rv


class InternalServerError(Exception):
    def __init__(self, message, status_code=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        rv = {}
        rv[MESSAGE] = self.message
        return rv

