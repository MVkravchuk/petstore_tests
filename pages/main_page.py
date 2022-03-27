import allure
from playwright.sync_api import Page

from model.user_model import User


class BasePage:

    def __init__(self, page: Page, base_url: str = 'https://petstore.swagger.io/') -> None:
        self.page = page
        self.base_url = base_url

    def load(self):
        self.page.goto(self.base_url)


class MainPage(BasePage):

    def __init__(self, page: Page, base_url: str = 'https://petstore.swagger.io/'):
        super().__init__(page, base_url)
        self.title = self.page.locator('h2')
        self.base_url_text = self.page.locator('.base-url')

    def create_user(self, user: User):
        with allure.step('Open method widget'):
            self.page.click("text=Create user")
        with allure.step('Add new user'):
            self.page.click("text=Try it out")
            with allure.step('Fill form'):
                self.page.locator("textarea").fill(user.to_json())
            self.page.locator("text=Execute").click()

    def delete_user(self, user: User):
        with allure.step('Open method widget'):
            self.page.click("text=Delete user")
        with allure.step('Delete user'):
            self.page.click("text=Try it out")
            with allure.step('Fill form'):
                self.page.locator('[placeholder="username"]').fill(user.username)
            self.page.locator("text=Execute").click()

        # TODO: Tag implementation for page elements
        # self.user_tag = self.page.locator('#swagger-ui > section > div.swagger-ui > div:nth-child(2) > div:nth-child(4) > section > div > span')\
        #     .locator(':has(#operations-tag-user)')
        # self.pet_tag = self.page.locator('#swagger-ui > section > div.swagger-ui > div:nth-child(2) > div:nth-child(4) > section > div > span')\
        #     .locator(':has(#operations-tag-pet)')
