from playwright.sync_api import Page


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
        self.user_tag = self.page.locator('#swagger-ui > section > div.swagger-ui > div:nth-child(2) > div:nth-child(4) > section > div > span')\
            .locator(':has(#operations-tag-user)')
        self.pet_tag = self.page.locator('#swagger-ui > section > div.swagger-ui > div:nth-child(2) > div:nth-child(4) > section > div > span')\
            .locator(':has(#operations-tag-pet)')