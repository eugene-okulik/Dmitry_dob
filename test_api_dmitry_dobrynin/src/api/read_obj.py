import requests
import allure

from test_api_dmitry_dobrynin.src.enums.global_enums import ErrorMessages
from test_api_dmitry_dobrynin.src.api.base_endpoint import BaseEndpoint


class GetObj(BaseEndpoint):

    @allure.step('Получение всех объектов')
    def read_all_obj(self):
        self.response = requests.get(self.URL)
        return self.response

    @allure.step('Получение одного объекта')
    def read_one_obj(self, obj_id: int):
        self.response = requests.get(f"{self.URL}/{obj_id}")
        return self.response

    def check_len_reponse_body(self, lenght):
        assert len(self.response.json()) == lenght, ErrorMessages.WRONG_LEN_OBJ.value

    def check_title_first_obj(self, name):
        assert self.response.json()['name'] == name, ErrorMessages.WRONG_TITLE.value
