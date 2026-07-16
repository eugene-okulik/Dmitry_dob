import requests
import allure

from test_api_dmitry_dobrynin.src.api.base_page import BasePage
from test_api_dmitry_dobrynin.src.enums.global_enums import ErrorMessages


class PostObj(BasePage):

    title_obj = None
    color = None
    size = None

    @allure.step('Создание объекта')
    def post_a_obj(self, data):
        self.title_obj, self.color, self.size = data
        body = {
            "name": self.title_obj,
            "data": {
                "color": self.color,
                "size": self.size
            }
        }
        self.response = requests.post(self.URL, json=body)
        self.id = self.response.json()['id']
        return self.response

    def check_title_create_obj(self):
        assert self.response.json()['name'] == self.title_obj, ErrorMessages.WRONG_TITLE.value

    def check_data_response(self):
        assert self.response.json()['data'] == {
            "color": self.color,
            "size": self.size}, ErrorMessages.WRONG_BODY.value
