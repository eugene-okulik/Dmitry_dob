import requests
import allure

from test_api_dmitry_dobrynin.src.api.base_endpoint import BaseEndpoint
from test_api_dmitry_dobrynin.src.enums.global_enums import ErrorMessages


class UpdateObj(BaseEndpoint):

    @allure.step('Полное обновление данных')
    def put_obj(self, body, id_obj):
        self.id = id_obj
        self.response = requests.put(
            f"{self.URL}/{self.id}",
            json=body
        )
        return self.response

    @allure.step('Частичное изменение объекта методом PATCH')
    def patch_obj(self, body, id_obj):
        self.id = id_obj
        self.response = requests.patch(
            f"{self.URL}/{self.id}",
            json=body
        )
        return self.response

    def check_body_name(self, name):
        assert self.response.json()['name'] == name, ErrorMessages.WRONG_TITLE.value

    def check_body(self, data):
        assert self.response.json()['data'] == data, ErrorMessages.WRONG_BODY.value

    def check_id(self):
        assert str(self.response.json()['id']) == str(self.id), ErrorMessages.WRONG_ID.value
