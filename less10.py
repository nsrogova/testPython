from selenium import (webdriver)
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.ID, "book)
WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button.click()


x_el = browser.find_element(By.ID, "input_value")
x = x_el.text
print(x)
y = calc(x)
print(y)
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)
button = browser.find_element(By.ID, "solve")
button.click()
time.sleep(5)
browser.quit()
