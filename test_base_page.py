import allure
import pytest
from locators.base_page_locators import URL, HOMEPAGE, SINGLE_ELEMENTS, INPUTS, COPYRIGHT_URL
from pages.base_page import BasePage



@allure.title("Клик по кнопке Homepage")
def test_first(browser):
    base_page = BasePage(browser)
    base_page.open_site(URL)
    base_page.click(HOMEPAGE)
    assert browser.current_url == URL


@pytest.mark.smoke
@allure.title("Клик по кнопке Single Elements")
def test_second(browser):
    base_page = BasePage(browser)
    base_page.open_site(URL)
    base_page.click(SINGLE_ELEMENTS)
    assert INPUTS


@pytest.mark.skip
@allure.title("Проверка, что отображается ссылка в футере")
def test_copyright_url_is_shown(browser):
    base_page = BasePage(browser)
    base_page.open_site(URL)
    base_page.click(SINGLE_ELEMENTS)
    assert base_page.get(COPYRIGHT_URL)
