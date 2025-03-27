import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nстарт браузера")
    browser = webdriver.Chrome()
    yield browser
    print("\nзакрытие браузера.")
    browser.quit()