from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

time.sleep(2)

try :
    accept_button = driver.find_element(By.XPATH, '//button/div[text()="Accept all"]')
    accept_button.click()
    print("Accept button clicked!")
except:
    print("Accept button not found.")

time.sleep(3)
driver.quit()