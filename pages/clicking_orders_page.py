from selenium.webdriver.common.by  import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page


SHOPCART = (By.CLASS_NAME,'nav-cart-icon nav-sprite')
AMZNORD = (By.ID,'nav-orders')
AMZNCE = (By.CLASS_NAME,'a-row')
AMZNSEARCH = (By.ID,'twotabsearchbox')
AMZNENTER = (By.ID,'nav-search-submit-button')
ADDTOCART = (By.ID,'add-to-cart-button')
MUG = (By.CLASS_NAME,'a-size-base-plus a-color-base a-text-normal')
INSHOPCART = (By.ID,'deselect-all')



class Amazon_orders:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = 'https://www.amazon.com/'

    def click(self, *AMZNORD):
        self.driver.find_element(*AMZNORD).click()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = 'https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fyour-orders%2Forders%2Fref%3Dyo_oh_gp_to_ov%3F_encoding%3DUTF8%26ref_%3Dnav_orders_first&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_retail_yourorders_us&openid.mode=checkid_setup&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0'

class ShoppingCart:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = 'https://www.amazon.com/'

    def click(self, *SHOPCART):
        self.driver.find_element(*SHOPCART).click()

    def verify_text(self, expected_text, *AMZNCE):
        actual_text = self.driver.find_element(*AMZNCE).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'


class Adding_to_ShoppingCart:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = 'https://www.amazon.com/'


    def find_element(self, *AMZNSEARCH):
        return self.driver.find_element(*AMZNSEARCH)


    def amazon_search(self,*AMZNSEARCH):
        self.driver.find_element(*AMZNSEARCH).send_keys('Mug')

    def click_search_icon(self,*AMZNENTER):
        self.driver.find_element(*AMZNENTER).click()

    def click_Mug(self,*MUG):
        self.driver.find_element(*MUG).click()

    def click_Mug(self,*ADDTOCART):
        self.driver.find_element(*ADDTOCART).click()

    def click(self, *SHOPCART):
        self.driver.find_element(*SHOPCART).click()

    def verify_text(self, expected_text, *INSHOPCART):
        actual_text = self.driver.find_element(*INSHOPCART).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
