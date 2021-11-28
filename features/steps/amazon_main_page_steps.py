from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon page')
def open_google(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for Anime')
def search_amazon(context, search_word):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Anime')


@when('Click search icon')
def click_search_icon(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()