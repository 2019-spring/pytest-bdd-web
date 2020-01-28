from selenium import webdriver
import pytest


class HeaderPanel():
    def __init__(self, browser):
        self.browser = browser
        self.search_box = browser.find_element_by_name("search_query")
        self.search_button = browser.find_element_by_name("submit_search")
        self.products = browser.find_elements_by_css_selector(
            ".center_column .product-name")

    def get_product_count(self, products):
        return len(products)

    def click_search_button(self, search_button):
        search_button.click()
