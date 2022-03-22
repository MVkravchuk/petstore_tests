import allure
import pytest
from hamcrest import assert_that, has_entries, equal_to

from helpers.servise import UserApiService
from model.user_model import User


@allure.suite('CRUD with users')
@allure.story('Add new user')
class TestCreateUser:

    @allure.title('Can create new unique user')
    def test_can_create_new_user(self):
        with allure.step("Add new user"):
            new_user = User().generate()
            response = UserApiService().create_user(new_user.to_dict())
        with allure.step("Validate response code"):
            assert response["code"] == 200

    @allure.title("Can't create new not unique user")
    @pytest.mark.skip("Skip this test")
    def test_cant_create_not_unique_user(self):
        with allure.step("Add new user"):
            new_user = User().generate()
            response = UserApiService().create_user(new_user.to_dict())
            assert response["code"] == 200
        with allure.step("Add same user"):
            response = UserApiService().create_user(new_user.to_dict())
            assert response["code"] == 500


@allure.suite('CRUD with users')
@allure.story('Read user info')
class TestReadUser:

    @allure.title('Can read user info from database by username')
    def test_can_get_user_by_user_name(self, new_user):
        with allure.step('Get user info'):
            response = UserApiService().get_user_by_username(new_user.username)
        with allure.step("Validate user data"):
            for key, value in new_user.to_dict().items():
                assert_that(response, has_entries(key, equal_to(value)))


@allure.suite('CRUD with users')
@allure.story('Delete user')
class TestDeleteUser:

    @allure.title('Can delete user by username (parametrize test)')
    @pytest.mark.parametrize(
        "user, result",
        [
            ('failed_test', 200),
            ("passed_test", 404),
        ],
    )
    def test_can_delete_user__by_user_name(self, user, result):
        with allure.step('Delete user'):
            response = UserApiService().delete_user(user)
            assert response.status_code == result
