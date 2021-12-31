from selenium.webdriver.common.by import By
from behave import when,given,then
from time import sleep

BST_SELLER = (By.XPATH,"//a[@href='/gp/bestsellers/ref=zg_bs_tab']")
NEW_RSLEASE = (By.XPATH,"//a[@href='/gp/new-releases/ref=zg_bs_tab']")
MVERS_SHKERS = (By.XPATH,"//a[@href='/gp/movers-and-shakers/ref=zg_bs_tab']")
MWFOR = (By.XPATH,"//a[@href='/gp/most-wished-for/ref=zg_bs_tab']")

@given('Open Amazon Best Sellers')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@when( 'User is sign in the homepage')
def click_on_Bestsellers(context):
    context.driver.find(*BST_SELLER).click()
    sleep(1)

@then('Verify user can click new releases links')
def verify_can_click_New_Releases(context):
    context.driver.find(*NEW_RSLEASE).click()
    sleep(1)

@then('Verify user can click movers and shakers links')
def verify_can_click_Movers_and_Shakers(context):
    context.driver.find(*MVERS_SHKERS).click()
    sleep(1)

@then('Verify user can click most wished for links')
def verify_can_click_Most_Wished_for(context):
    context.driver.find(*MWFOR).click()
    sleep(1)

