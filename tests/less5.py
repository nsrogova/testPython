import math
from selenium import (webdriver)
from selenium.webdriver.common.by import By
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
x_el = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_el.text
print(x)
y = calc(x)
print(y)
input1 = browser.find_element(By.CSS_SELECTOR, ".form-group > input")
input1.send_keys(y)
check = browser.find_element(By.CSS_SELECTOR, ".form-check-custom > input")
check.click()
radio = browser.find_element(By.CSS_SELECTOR, ".form-radio-custom > input")
radio.click()
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
time.sleep(10)
browser.quit()
