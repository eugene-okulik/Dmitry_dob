import pytest

from test_api_dmitry_dobrynin.src.api.read_obj import GetObj
from test_api_dmitry_dobrynin.src.api.create_obj import PostObj
from test_api_dmitry_dobrynin.src.api.update_obj import UpdateObj
from test_api_dmitry_dobrynin.src.api.delete_obj import DeleteObj


@pytest.fixture()
def read_objects():  # Для метода get
    return GetObj()


@pytest.fixture()
def create_obj():  # для метода post
    obj = PostObj()
    yield obj
    obj.clean_obj(obj.id)


@pytest.fixture()
def update_new_obj():  # для методов put and patch
    return UpdateObj()


@pytest.fixture()
def create_obj_id():  # Cоздание и удаление тестовой сущности
    data = ("Test object", "test_color", "test_size")
    obj = PostObj()
    response = obj.post_a_obj(data)
    id_obj = response.json()['id']
    yield id_obj
    obj.clean_obj(id_obj)


@pytest.fixture()  # для метода delete
def delete_obj():
    return DeleteObj()
