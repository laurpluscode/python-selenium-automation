from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

ANIME_MENU = (By.ID, 'nav-anime-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, "td.navFooterDescItem a")
SIGN_IN_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip a.nav-action-button")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    context.app.main_page.open()


@when('Search for Anime')
def search_amazon(context, search_word):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Anime')


#@when('Click search icon')
#def click_search_icon(context):
#    context.driver.find_element(By.ID, 'nav-search-submit-button').click()

#@when('Search for{keyword}')
def search_amazon(context,keyword):
    # context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(keyword)
    context.app.header.search_input(keyword)


#@when('Click search icon')
#def click_search_icon(context):
#context.driver.find_element(By.ID,'nav-search-submit-button').click()


@when('Click Orders')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@when('Click Sign In from popup')
def click_sign_in(context):
    e = context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN), message='Signin popup not clickable')
    e.click()

    element = context.driver.find_element(*SIGN_IN_BTN)
    print(element)
    context.driver.refresh()
    print(element)
    element.click()

# @then('Sign in pop up is visible')
# def verify_sign_popup_visible(context):
# context.driver.wait.until(EC.visibility_of_element_located(SIGN_IN_BTN),message ='Sign in popup not visible'

# @then('Sign in pop up disappears')
# def verify_sign_popup_disappear(context):
# context.driver.wait.until(EC.visibility_of_element_located(SIGN_IN_BTN),message ='Sign in popup not visible'

@when('Wait for {sec}sec')
def wait_sec(context,sec):
    sleep(int(sec))

@then('Verify Anime menu present')
def verify_anime_present(context):
    # element_count = len(context.driver.find_elements(*ANIME_MENU))
    # assert element_count == 1, f'Expect to see 1 option, but got {element_count}'
    context.driver.find_element(*ANIME_MENU)


@then('Verify {expected_amount} links present')
def verify_footer_link_amount(context):
    expected_amount = int(expected_amount)
    footer_links_amount = len(context.driver.find_elements(*FOOTER_LINKS))
