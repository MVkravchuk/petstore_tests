import requests
from hamcrest import assert_that, has_entries, equal_to

from helpers.servise import UserApiService
from model.user_model import User


class TestCreateUser:

    def test_can_create_new_user(self):
        new_user = User().generate()
        response = UserApiService().create_user(new_user.to_dict())
        assert response["code"] == 200

    def test_cant_create_not_unique_user(self):
        new_user = User().generate()
        response = UserApiService().create_user(new_user.to_dict())
        assert response["code"] == 200
        response = UserApiService().create_user(new_user.to_dict())
        assert response["code"] == 500


class TestReadUser:

    def test_can_get_user_by_user_name(self, new_user):
        response = UserApiService().get_user_by_username(new_user.username)
        for key, value in new_user.to_dict().items():
            assert_that(response, has_entries(key, equal_to(value)))