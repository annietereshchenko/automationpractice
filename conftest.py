import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    browser = webdriver.Chrome("C:/Users/Admin/PycharmProjects/TMS05_HW/chromedriver")
    browser.maximize_window()
    browser.implicitly_wait(5)
    browser.get('http://automationpractice.com/index.php')
    yield browser
    browser.quit()
