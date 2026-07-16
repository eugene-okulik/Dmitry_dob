import pytest
import allure
from faker import Faker
from random import choice

fake = Faker()

TEST_DATA = [
    (
        fake.sentence(nb_words=3),
        fake.color(),
        choice(['small', 'medium', 'large'])
    )
    for _ in range(3)
]


@allure.feature('Object')
@pytest.mark.minor
def test_get_all_obj(read_objects):
    read_objects.read_all_obj()
    read_objects.check_status_code_200()


@allure.feature('Object')
@pytest.mark.medium
def test_get_one_obj(read_objects):
    read_objects.read_one_obj(1)
    read_objects.check_status_code_200()
    read_objects.check_len_reponse_body()
    read_objects.check_title_first_obj()


@allure.feature('Object')
@allure.severity(allure.severity_level.CRITICAL)
@allure.issue(
    'http://mail.ru',
    'MK-3672 - При создании объекта неправильный статус код'
)
@allure.description(
    'Создание объектов с рандомном набором данных в кол-ве 3  шт.'
)
@pytest.mark.critical
@pytest.mark.parametrize('data', TEST_DATA)
def test_post_obj(create_obj, data):
    create_obj.post_a_obj(data)
    create_obj.check_status_code_200()
    create_obj.check_title_create_obj()
    create_obj.check_data_response()


@allure.feature('Object')
@pytest.mark.medium
def test_put_a_obj(update_new_obj, create_obj_id):
    update_new_obj.put_obj(id_obj=create_obj_id)
    update_new_obj.check_status_code_200()
    update_new_obj.check_body_name()
    update_new_obj.check_id()


@allure.feature('Object')
@pytest.mark.medium
def test_patch_a_obj(update_new_obj, create_obj_id):
    update_new_obj.patch_obj(id_obj=create_obj_id)
    update_new_obj.check_status_code_200()
    update_new_obj.check_body_name()
    update_new_obj.check_id()


@allure.feature('Object')
@pytest.mark.medium
def test_delete_obj(delete_obj, create_obj_id):
    delete_obj.delete_a_obj(id_obj=create_obj_id)
    delete_obj.check_status_code_200()
