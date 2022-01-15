from behave import when, then
from selenium.webdriver.common.by import By

CART = (By.ID, 'nav-cart-count')
PRODUCT_NAME = (By.CSS_SELECTOR, '#sc-active-cart li')


# @given('Open Amazon page')
# def open_google(context):
#    context.driver.get('https://www.amazon.com')

# look over

@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_count = context.driver.find_element(*CART).text
    assert actual_count == expected_count, f'Error, actual {actual_count} did not match {expected_count}'
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*PRODUCT_NAME).text
    assert context.product_name[:30] in actual_name, f'Expected {context.product_name}but go'
