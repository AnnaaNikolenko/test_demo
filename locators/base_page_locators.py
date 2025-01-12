from selenium.webdriver.common.by import By

HOMEPAGE = (By.XPATH, "//span[contains(text(), 'Homepage')]")
URL = "https://www.qa-practice.com/"
SINGLE_ELEMENTS = (By.XPATH, "//span[contains(text(), 'Single UI Elements')]")
INPUTS = (By.XPATH, "//a[@href='/elements/input']")
COPYRIGHT_URL = (By.XPATH, "//a[@href='https://www.qa-practice.com/']")