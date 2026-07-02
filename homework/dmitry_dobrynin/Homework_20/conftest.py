import requests
import pytest
from colorama import init, Fore

init(autoreset=True)

base_url = 'http://objapi.course.qa-practice.com/object'


@pytest.fixture()
def new_obj():  # setUp / tearDown
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
def clear_obj():  # отдельная функция для удаления сущностей
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
