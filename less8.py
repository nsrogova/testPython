from selenium import (webdriver)
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
button.click()
alert = browser.switch_to.alert
alert.accept()
x_el = browser.find_element(By.ID, "input_value")
x = x_el.text
print(x)
y = calc(x)
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
time.sleep(10)
browser.quit()
