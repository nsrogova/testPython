import math
from selenium import (webdriver)
from selenium.webdriver.common.by import By
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
x_el = browser.find_element(By.CSS_SELECTOR, "[src='images/chest.png']")
x = x_el.get_attribute('valuex')
print(x)
y = calc(x)
print(y)
input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
input1.send_keys(y)
check = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
check.click()
radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
radio.click()
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
time.sleep(10)
browser.quit()
