from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page

NWARRIVAL = (By.XPATH, "//a[@class='nav-content']")


class NewArrivals(Page):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = 'https://www.amazon.com/gp/product/B074TBCSC8'

    def find_element(self, *NWARRIVAL):
        return self.driver.find_element(*NWARRIVAL)

    def verify_New_arrivals(context):
        context.app.header.hover_lang()

    def hover_New_arrivals(self):
        NWARRIVAL = self.find_element()
        actions = ActionChains(self.driver)
        actions.move_to_element(*NWARRIVAL)

    def click(self, *NWARRIVAL):
        self.driver.find_element(*NWARRIVAL).click()
