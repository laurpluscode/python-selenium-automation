from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# Using classes
# 1 class:

driver.find_element(By.CSS_SELECTOR,"span.a-color-state")
driver.find_element(By.CSS_SELECTOR,".a-color-state")
# 2 or more
driver.find_element(By.CSS_SELECTOR,"span.a-color-state.a-text-bold")
driver.find_element(By.CSS_SELECTOR,".a-color-state.a-text-bold")
# Using attributes:
driver.find_element(By.CSS_SELECTOR,"a[href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie= UTF8&nodeID=508088")
# partial attr:
driver.find_element(By.CSS_SELECTOR,"a[href*='ap_signin_notification_condition_of_use")

driver.find_element(By.CSS_SELECTOR,"a.[href*='ap_signin_notification_condition_of_use")

# Go from parent to childern nodes:
driver.find_element(By.CSS_SELECTOR,"div#legalTextRow a[href*='ap_signin_notification_privacy_notice']")

# Class + attributes:
driver.find_element(By.CSS_SELECTOR,"a.nav[href='/gp/bestsellers/?ref=nav_cs_bestsellers_8a080d3d7b55497ea1bdd97b7cff8b7b']")
driver.find_element(By.CSS_SELECTOR,"a.nav[href='/gp/bestsellers/?ref=nav_cs_bestsellers_8a080d3d7b55497ea1bdd97b7cff8b7b'][data-csa-c-type='link']")
driver.find_element(By.CSS_SELECTOR,"a.nav[href*='nav_cs_bestsellers'][data-csa-c-type='link']")
