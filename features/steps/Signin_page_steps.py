from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')

@when ('Search for Returns and Orders')
def search_amazon(context):
    context.driver.find_element(By.ID, 'nav-orders').click()

