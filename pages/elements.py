from playwright.sync_api import Page


class BaseElement:

    def __init__(self, page: Page):
        self.page = page


class HandlerElement(BaseElement):

    def __init__(self, page: Page, ):
        super().__init__(page)
        self.root_element = self.page.locator('')
        self.method = page.locator('.opblock-summary-method')
        self.path = page.locator('.opblock-summary-parh')
        self.description = page.locator('.opblock-summary-description')
        self.try_out_bytton = page.locator('.try-out')
        self.response_description = page.locator('.responses-inner')
        self.request_body = page.locator('.body-param__text')


class TagElement(BaseElement):

    def __init__(self, page: Page):
        super().__init__(page)
        self.name = page.locator('.opblock-tag-section is-open')
        self.description = page.locator('.markdown')
        self.handlers = [handler for handler in [page.locator('operation-tag-content')]]
