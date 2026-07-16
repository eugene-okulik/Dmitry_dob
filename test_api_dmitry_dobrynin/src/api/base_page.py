import requests

from test_api_dmitry_dobrynin.src.enums.global_enums import ErrorMessages


class BasePage():

    URL = 'http://objapi.course.qa-practice.com/object'
    response = None
    id = None

    def check_status_code_200(self):
        assert self.response.status_code == 200, ErrorMessages.WRONG_STATUS_CODE.value

    def clean_obj(self, id_obj: int) -> None:
        self.id = id_obj
        return requests.delete(f"{self.URL}/{self.id}")
