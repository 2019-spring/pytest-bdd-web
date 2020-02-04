from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, browser):
        self.browser = browser
        self.wait = WW(self.browser, 10)

        self.search_box_id = 'search_query_top'

    def enter_search(self, text):
        search_box = self.wait.until(EC.presence_of_element_located(
            self.browser.find_element(By.ID, self.search_box_id)))
        search_box.clear()
        search_box.send_keys(text)
