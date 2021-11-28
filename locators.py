from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# By ID
driver.find_element(By.ID, 'twotabsearchtextbox')

# By XPATH
driver.find_element(By.XPATH, "//a[@href= '/ref =nav_logo']")
driver.find_element(By.XPATH, "//span[@class ='icp-nav-flag icp-nav-flag-us']")

# By XPATH, multiple attributes use (and).
driver.find_element(By.XPATH,
                    "//a [@class ='nav-a ' and @href= '/gp/bestsellers/? ref_=nav_cs_bestsellers_8a080d3d7b55497ea1bdd97b7cff8b7b']")
# By XPATH using  contains
driver.find_element(By.XPATH, "//a[contains(@href, '/gp/bestsellers/?ref_=nav_cs_bestsellers')]")

# using text
driver.find_element(By.XPATH, "//a[text() ='Best Sellers')")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class'nav-a')")
driver.find_element(By.XPATH, "//a[contains(text(),'Best Sell') and @class = 'nav-a ']")  # partial text

# using multiple nodes:
driver.find_element(By.XPATH,"//div[@id'=nav-xshop-container']//a[text() = 'Best Sellers']")
driver.find_element(By.XPATH,"//div[@id'=nav-xshop-container']/div[@id ='nav-x-shop']/a[text() = 'Best Sellers']")
driver.find_element(By.XPATH,"//select[@id ='searchDropDownBox']/option[@value='search-alias=audible']")

# only attribute
driver.find_element(By.XPATH, "//div")

driver.find_element(By.XPATH,"//select[@id ='searchDropDownBox']/option[@value='search-alias=audible']")