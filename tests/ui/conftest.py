import allure
import pytest
from playwright.sync_api import Page

from pages.main_page import MainPage


@allure.step('Open new page in browser')
@pytest.fixture()
def main_page(page: Page, url: str = 'https://petstore.swagger.io') -> MainPage:
    new_page = MainPage(page, url)
    new_page.load()
    return new_page


