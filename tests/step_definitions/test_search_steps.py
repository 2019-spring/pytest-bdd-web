from selenium import webdriver
import pytest
import time


# CONSTANTS
HOME_URL = "http://automationpractice.com/"


# Fixture
@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    time.sleep(5)
    yield
    driver.quit()

# STEPS


def test_start_home(browser):
    browser.get(HOME_URL)


def test_search_web(browser):
    # element locators
    search_box = browser.find_element_by_name("search_query")
    search_button = browser.find_element_by_name("submit_search")

    search_box.send_keys("dress")
    search_button.click()
