import time
import math

import pytest
from selenium.webdriver.common.by import By


from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nстарт браузера")
    browser = webdriver.Chrome()
    yield browser
    print("\nзакрытие браузера.")
    browser.quit()

login_link = "https://stepik.org/lesson/236905/step/1"


@pytest.fixture()
def test_config_login_link(browser):
    browser.get(login_link)
    browser.implicitly_wait(5)
    button = browser.find_element(By.ID, 'ember466')
    button.click()
    input1 = browser.find_element(By.ID, "id_login_email")
    input1.send_keys("sosnovaya_4@mail.ru")
    input2 = browser.find_element(By.ID, "id_login_password")
    input2.send_keys("Fuloza24!")
    button1 = browser.find_element(By.CSS_SELECTOR, '.button_with-loader')
    button1.click()
    print("фикстура завершена")


class TestFirst():
    links = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]
    messages = []

    # links = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]
    @pytest.mark.parametrize('link', links)
    def test_first1(self, browser, test_config_login_link, link):
        test_link = f"https://stepik.org/lesson/{link}/step/1"
        browser.get(test_link)
        browser.implicitly_wait(10)
        answer = math.log(int(time.time()))
        browser.find_element(By.TAG_NAME, "textarea").send_keys(str(answer))
        browser.find_element(By.CLASS_NAME, "submit-submission").click()
        hint = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
        time.sleep(10)
        if hint != "Correct!":
            self.messages.append(hint)
            print(self.messages)
        print(self.messages)