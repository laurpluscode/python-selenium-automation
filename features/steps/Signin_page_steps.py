from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

# @given('Open Amazon page')
# def open_amazon(context):
#    context.driver.get('https://www.amazon.com')

@when ('Search for Returns and Orders')
def search_amazon(context):
    context.driver.find_element(By.ID, 'nav-orders').click()

# Sign in with CSS selectors
# from selenium.webdriver.common.by import By
# from behave import given, when, then

# @then('Verify Sign in page opened')
# def verify_signin_opened(context):
   # context.driver.find_element(By.ID,'ap_email')
   # expected_header = 'Sign-In'
   # actual_header = context.driver.find_element(By.CSS_SELECTOR,"h1.a-spacing-small").text
    # assert expected_header == actual_header, f'Error! Expected {expected_header} but got {actual_header}

    assert 'https://www.amazon.com/ap/signin' in context.driver.current_url, f'https://www.amazon.com/ap/signin not in {context.driver.current_url}'

    context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'),message='...')