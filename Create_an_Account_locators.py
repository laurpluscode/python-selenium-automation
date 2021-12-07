from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Amazon Logo
driver.find_element(By.XPATH,"//a[@class ='a-icon a-icon-logo']")

# Create Account Logo
driver.find_element(By.XPATH,"//a[@class='a-spacing-small']")

# Your Name Input field
driver.find_element(By.XPATH,"//a[@class='a-input-text a-span12 auth-autofocus auth-required-field auth-contact-verification-request-info']")

# Your email Input field
driver.find_element(By.ID,'ap_email')

#Your Password
driver.find_element(By.ID,'ap_password')

# Your Re-enter password
driver.find_element(By.ID,'ap_password_check')

# Passwords must be at least 6 characters.
driver.find_element(By.XPATH,"//a[@class='a-alert-content']")

# Create your Amazon Account
driver.find_element(By.XPATH,"//a[@class='a-button-input']")

# Conditions of Use
driver.find_element(By.XPATH,"//a[@href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&amp;nodeId=508088']")

# Privacy Notice
driver.find_element(By.XPATH,"//a[@href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&amp;nodeId=468496']")

# Sign in
driver.find_element(By.XPATH,"//a[@class='a-link-emphasis' and @href='/ap/signin?openid.pape.max_auth_age=0&amp;openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&amp;prevRID=FVHY9343PXXCZAAJQ54S&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.assoc_handle=usflex&amp;openid.mode=checkid_setup&amp;failedSignInCount=0&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;pageId=usflex&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0']")