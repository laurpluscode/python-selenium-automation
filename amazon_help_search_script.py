from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/Users/LaurenIT/Documents/GitHub/python-selenium-automation/chromedriver')

driver.get('https://www.amazon.com/gp/help/customer/display.html')

driver.find_element(By.ID, 'helpsearch').send_keys("Cancel Items")

driver.find_element(By.ID, 'helpsearch').send_keys(Keys.ENTER)

# actual_result = driver.find_element(By.XPATH,"//p[@class='a-color-secondary']")
actual_result = driver.find_element(By.XPATH,"//div[@class='help-content']/h1").text
expected_result = 'Cancel items or Orders'
# expected_result = driver.find_element(By.XPATH,"//p[@class='a-color-secondary']")

assert actual_result == expected_result, f'Error {actual_result} did not match {expected_result}'
print('Test Case Passed')
driver.quit()