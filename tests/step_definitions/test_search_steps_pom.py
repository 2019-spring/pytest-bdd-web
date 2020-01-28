from selenium import webdriver
import pytest
import time
from pytest_bdd import scenarios, given, when, then, parsers
from pages.home_page import HeaderPanel as hpanel

# CONSTANTS
HOME_URL = "http://automationpractice.com/"

# scenarios
scenarios("../features/search.feature")

# STEPS
@given("the store home page is displayed")
def test_start_home(browser):
    print('home page starting..')
    browser.get(HOME_URL)
    time.sleep(5)


@when(parsers.parse("the user searches for {phrase}"))
def test_search_web(browser, phrase):
    print('search is staritng')
    hpanel.search_box.send_keys(phrase)
    hpanel.click_search_button()
    print('done')


@then("at least one product is listed")
def test_verify_products_list(browser):
    assert hpanel.get_product_count() >= 1
    print('search result verified')
