from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
time.sleep(2)

username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "user-name"))
)
username_field.send_keys("standard_user")

password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "password"))
)
password_field.send_keys("secret_sauce")

login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "login-button"))
)
login_button.click()

print("Login successfully!")

time.sleep(3)
driver.quit()
