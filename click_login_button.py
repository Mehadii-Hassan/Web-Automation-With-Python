from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/howto/howto_css_login_form.asp")
time.sleep(2)

try :
    login_button = driver.find_element(By.XPATH, '//button[text()="Login"]')
    login_button.click()
except Exception as e :
    print("Button not found.", e)

time.sleep(2)
driver.quit()