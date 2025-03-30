from rest_framework.exceptions import APIException

class CustomAPIException(APIException):
    status_code = 400  # default to bad request
    default_detail = 'A server error occurred.'

    def __init__(self, detail=None, status_code=None):
        if status_code is not None:
            self.status_code = status_code
        if detail is not None:
            self.detail = {'success': False, 'message': detail}
