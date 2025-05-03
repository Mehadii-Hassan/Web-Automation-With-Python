from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")
time.sleep(2)

try :
    submit_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
    submit_button.click()
    print("Submit button click successfully.")
except Exception as e :
    print("Something Error", e)

time.sleep(3)
driver.quit()