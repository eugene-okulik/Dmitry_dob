import requests
import pytest
from random import choice
from colorama import init, Fore
from faker import Faker

init(autoreset=True)
fake = Faker()

base_url = 'http://objapi.course.qa-practice.com/object'
error_status_code = 'status code incorrect'
error_len_object = 'len incorrect'
error_title = 'name object incorrect'
error_body = 'response body incorrect'


@pytest.fixture()
def new_post():  # setUp / tearDown
    body = {
        "name": "Test object",
        "data": {
            "color": "test_color",
            "size": "test_size"
        }
    }
    response = requests.post(
        base_url,
        json=body
    )
    id = response.json()['id']
    yield str(id)
    requests.delete(base_url + '/' + f"{id}")


@pytest.fixture()
def clear_post():  # отдельная функция для удаления сущностей
    ids = []
    yield ids
    for id in ids:
        requests.delete(base_url + '/' + f"{id}")


@pytest.fixture(scope="session")
def log_all_test():
    print(Fore.YELLOW + 'Start testing')
    yield
    print(Fore.YELLOW + '\nTesting completed')


@pytest.fixture(autouse=True)
def log_test():
    print('before test')
    yield
    print('\nafter test')


@pytest.mark.minor
def test_get_all_posts(log_all_test):  # Получение списка всех объектов
    response = requests.get(base_url)
    assert response.status_code == 200, error_status_code


@pytest.mark.medium
def test_get_one_post(new_post):  # Получение одного объекта по id
    id = new_post
    response = requests.get(base_url + '/' + str(id))
    assert response.status_code == 200, error_status_code
    assert len(response.json()) == 3, error_len_object
    assert response.json()['name'] == 'Test object', error_title


test_data = [
    (fake.sentence(nb_words=3), fake.color(), choice(['small', 'medium', 'large']))
    for _ in range(3)
]


@pytest.mark.critical
@pytest.mark.parametrize('title_obj, color, size', test_data)
def test_post_a_post(clear_post, title_obj, color, size):  # Добавление нового объекта
    body = {
        "name": title_obj,
        "data": {
            "color": color,
            "size": size
        }
    }
    response = requests.post(
        base_url,
        json=body
    )
    assert response.status_code == 200, error_status_code
    id = response.json()['id']
    clear_post.append(id)
    assert response.json()['name'] == title_obj, error_title
    assert response.json()['data'] == {
        "color": color, "size": size
    }, error_body


@pytest.mark.medium
def test_put_a_post(new_post):  # Полное изменение существующего объекта
    need_id = new_post
    body = {
        "name": "Test object - UPD_PUT",
        "data": {
            "color": "test_color - UPD_PUT",
            "size": "test_size - UPD_PUT"
        }
    }
    response = requests.put(
        base_url + '/' + need_id,
        json=body
    )
    assert response.status_code == 200, error_status_code
    assert response.json()['name'] == "Test object - UPD_PUT", error_title
    assert response.json()['data'] == {
        "color": "test_color - UPD_PUT",
        "size": "test_size - UPD_PUT"
    }, error_body
    assert response.json()['id'] == need_id, error_body


@pytest.mark.medium
def test_patch_a_post(new_post):  # Частичное изменение существующего объекта
    need_id = new_post
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


@pytest.mark.medium
def test_delete_a_post(new_post):  # Удаление существующего объекта
    need_id = new_post
    response = requests.delete(base_url + '/' + need_id)
    assert response.status_code == 200, error_status_code
