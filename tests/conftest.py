from model.user_model import User
import pytest
import allure


@allure.step('Create new user')
@pytest.fixture(scope="function")
def new_user() -> User:
    return User().create()
