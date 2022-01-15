from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# init driver
driver = webdriver.Chrome(executable_path='/Users/LaurenIT/Documents/GitHub/python-selenium-automation/chromedriver')
driver.maximize_window()
driver.implicitly_wait(4)
driver.wait
# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('watches')

# wait for 4 sec
sleep(4)

# click search
element = driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')), message='Search button not found')
driver.find_element(By.NAME, 'btnK').click()

# verify
assert 'watches' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
