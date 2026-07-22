from test_api_dmitry_dobrynin.src.enums.global_enums import ErrorMessages


class BaseEndpoint():

    URL = 'http://objapi.course.qa-practice.com/object'
    response = None
    id = None

    def check_status_code_200(self):
        assert self.response.status_code == 200, ErrorMessages.WRONG_STATUS_CODE.value
