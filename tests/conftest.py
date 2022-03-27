from playwright.sync_api import Page

from model.user_model import User
import pytest
import allure

from pages.main_page import MainPage


@allure.step("Create new user")
@pytest.fixture(scope="function")
def new_user() -> User:
    return User().create()


@allure.step("Generate fake user")
@pytest.fixture(scope="function")
def fake_user() -> User:
    return User().generate()
