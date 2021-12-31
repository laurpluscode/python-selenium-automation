from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

DOG_IMG = (By.CSS_SELECTOR, "img#d")


@given('Store original window')
def store_window(context):
    context.original_window = context.driver.current_window_handle
    print('Original window:', context.orginal_window)


@when('Click on a dog image')
def click_dog_img(context):
    context.driver.find_element(*DOG_IMG).click()


@when('Switch to new window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window.handles
    context.driver.switch_to.window(windows[1])

@then('Verify blog is opened')
def verify_blog_opened(context):
    assert 'https://www.aboutamazon.com/' in context.driver.current_url,f'Blog page did not open'

@then('Close blog')
def close_blog(context):
    context.driver.close()

@then('Return to original window')
def return_to_original_window(context):
    context.driver.switch_to.window(context.original_window)