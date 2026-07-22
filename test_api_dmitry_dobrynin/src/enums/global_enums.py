from enum import Enum


class ErrorMessages(Enum):

    WRONG_STATUS_CODE = 'status code incorrect'
    WRONG_LEN_OBJ = 'len incorrect'
    WRONG_TITLE = 'name object incorrect'
    WRONG_BODY = 'response body incorrect'
    WRONG_ID = 'id object incorrect'
