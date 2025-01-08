import allure
from locators.base_page_locators import URL, HOMEPAGE, SINGLE_ELEMENTS, INPUTS
from pages.base_page import BasePage


@allure.title("Клик по кнопке Homepage")
def test_click_homepage(browser):
    base_page = BasePage(browser)
    base_page.open_site(URL)
    base_page.click(HOMEPAGE)
    assert browser.current_url == URL


@allure.title("Клик по кнопке Single Elements")
def test_click_single_elements(browser):
    base_page = BasePage(browser)
    base_page.open_site(URL)
    base_page.click(SINGLE_ELEMENTS)
    assert INPUTS
