from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return WebDriverWait(self.driver, timeout=40).until(EC.element_to_be_clickable(locator),
                                                            message=f"Element is NOT CLICKABLE{locator}")

    def open_site(self, url):
        self.driver.get(url)

    def click(self, homepage):
        self.find_element(homepage).click()

    def get(self, locator):
        return self.find_element(locator).text
