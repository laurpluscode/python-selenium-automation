from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import Page


class AmazonDepartment(Page):
    DDD = (By.ID, 'searchDropdownBox')
    BOOKDP = (By.XPATH, "//a[@value='288Y76QJ9UASF']")


def get_category_locator(self):
    return [self.SUB[0], self.SUB_NAV[1].replace()]


def select_department(self):
    dropdown = self.find_element(*self.DDD)
    select = Select(dropdown)
    select.select_by_value('search-alias=stripbooks')


def hover_department(self):
    BOOKDP = self.find_element()
    actions = ActionChains(self.driver)
    actions.move_to_element(*BOOKDP)
    actions.click()


def verify_correct_department(self, BOOKDP):
    self._get_category_locator(*BOOKDP)
    self.wait_for_element_appear(*BOOKDP)
