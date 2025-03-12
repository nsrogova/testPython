
from selenium import (webdriver)
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
x_el = browser.find_element(By.CSS_SELECTOR, "#num1")
x = x_el.text
print(x)
y_el = browser.find_element(By.CSS_SELECTOR, "#num2")
y = y_el.text
print(y)
sum1 = int(x) + int(y)
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(sum1))
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
time.sleep(10)
browser.quit()
