from behave import given, when
from selenium.webdriver.common.by import By


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when('Search for table')
def search_amazon(context):
    context.driver.find_element(By.ID, 'twotabsearch').send_keys('table')


@when('Click search icon')
def click_search_icon(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()

# Sign in with Xpath
# from selenium.webdriver.common.by import By
# from behave import given, when, then

# @then('Verify Sign in page opened')
# def verify_search_results(context,expected_result):
# expected_header = 'Sign-In'
# actual_header = context.driver.find_element(By.XPATH,"//span[@class='a-color-state a text-bold']").text
# assert actual_result == expected_result, f'Error, actual {actual_result} did not match {expected_results}

# @then('Verify {category} department is selected')
# def verify_department(context,category):
#   context.app.search_results_page.verify_correct_department(category)
