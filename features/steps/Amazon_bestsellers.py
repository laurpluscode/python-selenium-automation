from selenium.webdriver.common.by import By
from behave import when,given,then
from time import sleep

BST_SELLER = (By.XPATH,"//a[@href='/gp/bestsellers/ref=zg_bs_tab']")
NEW_RSLEASE = (By.XPATH,"//a[@href='/gp/new-releases/ref=zg_bs_tab']")
MVERS_SHKERS = (By.XPATH,"//a[@href='/gp/movers-and-shakers/ref=zg_bs_tab']")
MWFOR = (By.XPATH,"//a[@href='/gp/most-wished-for/ref=zg_bs_tab']")
GFT_IDEAS = (By.XPATH,"//a[@href='/gp/most-gifted/ref=zg_bs_tab']")

@given('User is sign in the homepage')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/css/homepage.html?ref_=nav_youraccount_btn')

@when('User is sign in the homepage')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@when('verify if link one is Best sellers')
def verify_Bestsellers(context):
    context.driver.find_element(*BST_SELLER).click()
    sleep(1)

@when('verify if link two is New Release')
def verify_New_Releases(context):
    context.driver.find_element(*NEW_RSLEASE).click()
    sleep(1)

@when('verify if link three is Movers & Shakers')
def verify_Movers_Shakers(context):
    context.driver.find_element(*MVERS_SHKERS).click()
    sleep(1)

@when('verify if link four is Most Wished For')
def verify_Most_Wished_for(context):
    context.driver.find_element(*MWFOR).click()
    sleep(1)

@then('Verify is link five is Gift Ideas')
def verify_gift_ideas(context):
    context.driver.find(*GFT_IDEAS).click()
    sleep(1)