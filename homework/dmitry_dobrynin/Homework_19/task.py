import requests

base_url = 'http://objapi.course.qa-practice.com/object'
error_status_code = 'status code incorrect'
error_len_object = 'len incorrect'
error_title = 'name object incorrect'
error_body = 'response body incorrect'


def test_get_all_posts():  # Получение списка всех объектов
    response = requests.get(base_url)
    assert response.status_code == 200, error_status_code


test_get_all_posts()


def test_get_one_post(id):  # Получение одного объекта по id
    response = requests.get(base_url + '/' + str(id))
    assert response.status_code == 200, error_status_code
    assert len(response.json()) == 3, error_len_object
    assert response.json()['name'] == 'First object', error_title


test_get_one_post(1)


def clear_a_post(id):  # функция для чистки ненужных сущностей
    response = requests.delete(base_url + '/' + f"{id}")
    return response.status_code


def test_post_a_post():  # Добавление нового объекта
    body = {
        "name": "Second object",
        "data": {
            "color": "black",
            "size": "small"
        }
    }
    response = requests.post(
        base_url,
        json=body
    )
    assert response.status_code == 200, error_status_code
    assert response.json()['name'] == "Second object", error_title
    assert response.json()['data'] == {
        "color": "black", "size": "small"
    }, error_body
    assert 'id' in response.json(), error_body
    clear_a_post(response.json()['id'])


test_post_a_post()


def create_a_test_post():  # функция для создания сущности изменения
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
    return str(response.json()['id'])


def test_put_a_post():  # Полное изменение существующего объекта
    need_id = create_a_test_post()
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
    clear_a_post(need_id)


test_put_a_post()


def test_patch_a_post():  # Частичное изменение существующего объекта
    need_id = create_a_test_post()
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
    clear_a_post(need_id)


test_patch_a_post()


def check_delete(id):  # Функция для проверки отсутствия сущности
    response = requests.get(base_url + '/' + id)
    return response.status_code


def test_delete_a_post():  # Удаление существующего объекта
    need_id = create_a_test_post()
    response = requests.delete(base_url + '/' + need_id)
    assert response.status_code == 200, error_status_code
    assert check_delete(need_id) == 404, error_status_code


test_delete_a_post()
