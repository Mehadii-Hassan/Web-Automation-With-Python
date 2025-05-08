from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")
time.sleep(2)

driver.find_element(By.NAME, "username").send_keys("mehedi32")
driver.find_element(By.NAME, "password").send_keys("securePass456")

driver.find_element(By.NAME, "comments").clear()
driver.find_element(By.NAME, "comments").send_keys("This is a test comment by Mehedi.")

checkbox = driver.find_element(By.XPATH, '//input[@value="cb1"]')
if not checkbox.is_selected():
    checkbox.click()

driver.find_element(By.XPATH, '//input[@value="rd2"]').click()

dropdown = Select(driver.find_element(By.NAME, "dropdown"))
dropdown.select_by_visible_text("Drop Down Item 5")

driver.find_element(By.NAME, "submitbutton").click()

print("Form successfully submitted!")

time.sleep(3)
driver.quit()