import requests
import allure

from test_api_dmitry_dobrynin.src.api.base_page import BasePage


class DeleteObj(BasePage):

    @allure.step('Удаление объекта')
    def delete_a_obj(self, id_obj):
        self.response = requests.delete(f"{self.URL}/{id_obj}")
