from playwright.sync_api import Page, expect
import pytest
from model.user_model import User
from pages.main_page import MainPage

@pytest.fixture()
def main_page(page: Page, url: str = 'https://petstore.swagger.io') -> MainPage:
    foo = MainPage(page, url)
    foo.load()
    return foo

# test_my_application.py
def test_can_open_the_main_page(main_page: MainPage, new_user: User):
    expect(main_page.title).to_be_visible()
    assert main_page.title.inner_text() == 'Swagger Petstore\n 1.0.6 '
    expect(main_page.base_url_text).to_be_visible()
    assert main_page.base_url_text.inner_text() == '[ Base URL: petstore.swagger.io/v2 ]'

    # expect(main_page.user_tag).to_have_count(3)

    # page.click("text=Create user")
    # page.click("text=Try it out")
    # assert page.is_visible('text=This can only be done by the logged in user.')
    # user = new_user.to_json()
    # page.locator("textarea").fill(user)
    # page.locator("text=Execute").click()
    # expect(page.locator('.responses-inner')).to_be_visible()




# def test_with_pageobject(page: Page, main_page):
#     assert main_page.page.inner_text('h2') == 'Swagger Petstore\n 1.0.6 '
#     # tag = TagElement(main_page.page)
#     # expect(tag.name.inner_text('h3')).to_have_text('pet')
#     # main_page.page.click("text=Create user")
#     foo = main_page.page.locator("text=Delete user")
#     baz = main_page.page.locator(
#         '.operation-tag-content')
#     bar = main_page.page.locator("#swagger-ui > section > div.swagger-ui > div:nth-child(2) > div:nth-child(4) > section > div > span:nth-child(1) > div > div > div")
#     baz.locator('.opblock-summary')
#     main_page.page.click('#operations-user-createUser div:has-text("Try it out") >> nth=4')
#     x = baz.locator('.opblock-summary:has-text("Creates list of users with given input array")').all_inner_texts()
#     x = baz.locator('.opblock-summary').locator(':has-text("Creates list of users with given input array")').all_inner_texts()

#operations-user-createUser > div.no-margin > div > div.opblock-section > div.opblock-section-header > div.try-out
# //*[@id="operations-user-createUser"]/div[2]/div/div[2]/div[1]/div[2]