from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.CSS_SELECTOR, ".first_class > input")
input1.send_keys("Ivan")
input2 = browser.find_element(By.CSS_SELECTOR, ".second_class > input")
input2.send_keys("Petrov")
input3 = browser.find_element(By.CSS_SELECTOR, ".third_class > input")
input3.send_keys("Smolensk")

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(1)

welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
welcome_text = welcome_text_elt.text

assert "Congratulations! You have successfully registered!" == welcome_text

time.sleep(10)
browser.quit()
