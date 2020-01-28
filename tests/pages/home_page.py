from selenium import webdriver
import pytest
from basePage import BasePage


class HeaderPanel(BasePage):
    def __init__(self, browser):
        self.browser = browser
        self.search_box = browser.find_element_by_name("search_query")
        self.search_button = browser.find_element_by_name("submit_search")
        self.products = browser.find_elements_by_css_selector(
            ".center_column .product-name")

    def get_product_count(self):
        return len(self.products)

    def click_search_button(self):
        self.search_button.click()

    def clear_search_box(self):
        self.search_box.clear()
