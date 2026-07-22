import requests
import allure

from test_api_dmitry_dobrynin.src.api.base_endpoint import BaseEndpoint


class DeleteObj(BaseEndpoint):

    @allure.step('Удаление объекта')
    def delete_a_obj(self, id_obj):
        self.response = requests.delete(f"{self.URL}/{id_obj}")
