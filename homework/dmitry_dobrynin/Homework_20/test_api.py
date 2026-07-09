import requests
import pytest
import allure
from random import choice
from faker import Faker


fake = Faker()

base_url = 'http://objapi.course.qa-practice.com/object'
error_status_code = 'status code incorrect'
error_len_object = 'len incorrect'
error_title = 'name object incorrect'
error_body = 'response body incorrect'


@allure.feature('Object')
@allure.story('Получение данных')
@allure.title('Получение списка всех объектов')
@pytest.mark.minor
def test_get_all_obj(log_all_test):  # Получение списка всех объектов
    response = requests.get(base_url)
    assert response.status_code == 200, error_status_code


@allure.feature('Object')
@allure.story('Получение данных')
@allure.title('Получение получение одного объекта по id')
@pytest.mark.medium
def test_get_one_obj(new_obj):  # Получение одного объекта по id
    id = new_obj
    response = requests.get(base_url + '/' + str(id))
    assert response.status_code == 200, error_status_code
    assert len(response.json()) == 3, error_len_object
    assert response.json()['name'] == 'Test object', error_title


test_data = [
    (
        fake.sentence(nb_words=3),
        fake.color(),
        choice(['small', 'medium', 'large'])
    )
    for _ in range(3)
]


@allure.feature('Object')
@allure.story('Создание данных')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Создание объекта')
@allure.issue(
    'http://mail.ru',
    'MK-3672 - При создании объекта неправильный статус код'
)
@allure.description(
    'Создание объектов с рандомном набором данных в кол-ве 3  шт.'
)
@pytest.mark.critical
@pytest.mark.parametrize('title_obj, color, size', test_data)
def test_post_a_obj(clear_obj, title_obj, color, size):  # Добавление объекта
    with allure.step(
        f"Подготовка данных к тесту {title_obj}, {color}, {size}"
    ):
        body = {
            "name": title_obj,
            "data": {
                "color": color,
                "size": size
            }
        }
    with allure.step("Выполнение запроса"):
        response = requests.post(
            base_url,
            json=body
        )
    with allure.step("Проверка статус кода"):
        assert response.status_code == 201, error_status_code
    id = response.json()['id']
    clear_obj.append(id)
    with allure.step("Проверка тела ответа"):
        assert response.json()['name'] == title_obj, error_title
        assert response.json()['data'] == {
            "color": color, "size": size
        }, error_body


@allure.feature('Object')
@allure.story('Изменение данных')
@allure.title('Изменение объекта методом PUT')
@pytest.mark.medium
def test_put_a_obj(new_obj):  # Полное изменение существующего объекта
    with allure.step("Получение id объекта и подготовка данных"):
        need_id = new_obj
        body = {
            "name": "Test object - UPD_PUT",
            "data": {
                "color": "test_color - UPD_PUT",
                "size": "test_size - UPD_PUT"
            }
        }
    with allure.step("Выполнение запроса"):
        response = requests.put(
            base_url + '/' + need_id,
            json=body
        )
    with allure.step("Проверка статус кода"):
        assert response.status_code == 200, error_status_code
    with allure.step("Проверка тела ответа"):
        assert response.json()['name'] == "Test object - UPD_PUT", error_title
        assert response.json()['data'] == {
            "color": "test_color - UPD_PUT",
            "size": "test_size - UPD_PUT"
        }, error_body
        assert response.json()['id'] == need_id, error_body


@allure.feature('Object')
@allure.story('Изменение данных')
@allure.title('Изменение объекта методом PATCH')
@pytest.mark.medium
def test_patch_a_post(new_obj):  # Частичное изменение существующего объекта
    need_id = new_obj
    body = {
        "name": "Test object - UPD_PATCH",
    }
    response = requests.patch(
        base_url + '/' + need_id,
        json=body
    )
    assert response.status_code == 200, error_status_code
    assert response.json()['name'] == "Test object - UPD_PATCH", error_title
    assert response.json()['id'] == int(need_id), error_body


@allure.feature('Object')
@allure.story('Удаление данных')
@allure.title('Удаление объекта')
@pytest.mark.medium
def test_delete_a_obj(new_obj):  # Удаление существующего объекта
    need_id = new_obj
    response = requests.delete(base_url + '/' + need_id)
    assert response.status_code == 200, error_status_code
