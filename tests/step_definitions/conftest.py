import pytest
from selenium import webdriver



@pytest.fixture(scope='module')
def browser():
    chrome_opt = webdriver.ChromeOptions()
    chrome_opt.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_opt)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
