from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#Amazon logo
driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-logo']")

#Continue button
driver.find_element(By.ID,'continue')

#Need help link
driver.find_element(By.XPATH,"//span[@class='a-expander-prompt']")

#Forgot your password link
driver.find_element(By.ID,'auth-fpp-link-bottom')

#Other issues with Sign-In link
driver.find_element(By.ID,'ap-other-signin-issues-link')

#Create your Amazon account button
driver.find_element(By.ID,'createAccountSubmit')

#Conditions of use link
driver.find_element(By.XPATH,"//a[contains (@href,’ap_desktop_footer_cou’]")
#Privacy Notice link
driver.find_element(By.XPATH,"//a[contains(@href,’ap_desktop_footer_cou’),and @class=‘a-link-normal’]")
