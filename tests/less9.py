from selenium import (webdriver)
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")
button.click()
window_name = browser.window_handles[1]
browser.switch_to.window(window_name)
time.sleep(1)
x_el = browser.find_element(By.ID, "input_value")
x = x_el.text
print(x)
y = calc(x)
print(y)
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
time.sleep(5)
browser.quit()
