import requests
import allure

from test_api_dmitry_dobrynin.src.api.base_page import BasePage
from test_api_dmitry_dobrynin.src.enums.global_enums import ErrorMessages


class UpdateObj(BasePage):

    @allure.step('Полное обновление данных')
    def put_obj(self, id_obj):
        self.id = id_obj
        body = {
            "name": "Test object - UPD",
            "data": {
                "color": "test_color - UPD",
                "size": "test_size - UPD"
                }
            }
        self.response = requests.put(
            f"{self.URL}/{self.id}",
            json=body
        )
        return self.response

    @allure.step('Частичное изменение объекта методом PATCH')
    def patch_obj(self, id_obj):
        self.id = id_obj
        body = {
            "name": "Test object - UPD"
            }
        self.response = requests.patch(
            f"{self.URL}/{self.id}",
            json=body
        )
        return self.response

    def check_body_name(self):
        assert self.response.json()['name'] == "Test object - UPD", ErrorMessages.WRONG_TITLE.value

    def check_body(self):
        assert self.response.json()['data'] == {
            "color": "test_color - UPD",
            "size": "test_size - UPD"
        }, ErrorMessages.WRONG_BODY.value

    def check_id(self):
        assert str(self.response.json()['id']) == str(self.id), ErrorMessages.WRONG_ID.value
