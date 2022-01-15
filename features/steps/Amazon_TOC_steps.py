from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

PRIV_LINK = (By.XPATH, "//a[@href='https://www.amazon.com/privacy']")


@given('Open Amazon T&C page')
def open_google(context):
    context.driver.get(
        'https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088 ')


@when('Store original windows')
def store_o_window(context):
    context.driver.original_window = context.driver.current_window_handle
    print('Original window:', context.driver.original_window)


@when('Click on Amazon Privacy Notice link')
def privacy_notice_link(context):
    context.driver.find_element(*PRIV_LINK).click()


@when('Switch to the newly opened window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    context.driver.switch_to.window(windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def verify_page_opened(context):
    #    print(context.driver.current_url)
    assert 'https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ' in context.driver.current_url, f'Privacy page did not open'


@then('User can close new window and switch back to original')
def return_to_original_window2(context):
    context.driver.switch_to.window(context.driver.original_window)
