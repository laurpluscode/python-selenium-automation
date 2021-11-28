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
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[4]/div[2]/a[2]")
#Needs better Xpressions?-
#driver.find_element(By.XPATH,"//a[@class='a-link-normal' target='_blank' rel='noopener' and @href='/gp/help/customer/display.html/ref=ap_desktop_footer_cou?ie=UTF8&amp;nodeId=508088']")

#Privacy Notice link
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[4]/div[2]/a[2]")
#Needs better Xpressions?-
#driver.find_element(By.XPATH,"//a[@class ='a-link-normal' and @target ='_blank' rel='noopener' and @href=<a class="a-link-normal" target="_blank" rel="noopener" @href='/gp/help/customer/display.html/ref=ap_desktop_footer_privacy_notice?ie=UTF8&amp;nodeId=468496']")
