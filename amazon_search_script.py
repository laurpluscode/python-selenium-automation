from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/LaurenIT/Documents/GitHub/python-selenium-automation/chromedriver')

driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys("Anime")

driver.find_element(By.ID, 'nav-search-submit-button').click()

actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
expected_result = '"Anime"'

assert actual_result == expected_result, f'Error {actual_result} did not match {expected_result}'
print('Test Case Passed')
driver.quit()
