from selenium.webdriver.common.by import By
from behave import when, given, then
from time import sleep

ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
COLOR_OPTIONS = (By.CSS_SELECTOR, '"#variation_color_name li"')
SELECTED_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')


@given('Open Amazon product{product_id}page')
def open_amazon(context, product_id):
    """

    :type product_id: str
    :param context:
    """
    context.driver.get('https://www.amazon.com/dp/{product_id}')


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find(*ADD_TO_CART_BTN).click()
    sleep(1)


@then('Verify user can click through colors')
def verify_can_click_colors(context):
    expected_colors = ['Black-1', 'Dark Blue', 'Red Wine']

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    # for i in range(len(colors)):
    #    colors[i].click()
    #   actual_color = context.driver.find_element(* SELECTED_COLOR).text
    #   assert actual_color == expected_colors[i], f'Expected{expected_colors[i]},but got {actual_color}'
    actual_colors = []
    for color in colors[:1]:
        color.click()
        actual_colors += [context.driver.find_element(*SELECTED_COLOR).text]
        print(actual_colors)

    assert actual_colors == expected_colors, f'Expected {expected_colors}but got {actual_colors}'
