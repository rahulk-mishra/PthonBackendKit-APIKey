class APIException(Exception):
    def __init__(self, http_response_code=None, status=None, error_code=None, error_message=None):
        super().__init__(error_message or error_code or "Something went wrong")
        self.http_response_code = http_response_code
        self.status = status
        self.error_code = error_code
        self.error_message = error_message