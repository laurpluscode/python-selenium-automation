from selenium.webdriver.common.by import By

from pages.base_page import Page


class Header(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    FLAG = (By.CSS_SELECTOR, 'icp-nav-flag.icp-nav-flag-us')
    DEPARTMENT_DROPDOWN = (By.ID, 'searchDropdownbox')

    def search_input(self, text):
        self.input_text(text, *self.SEARCH_INPUT)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def select_department(self):
        dropdown = self.find_element(*self.DEPARTMENT_DROPDOWN)
        select = select(dropdown)
        select.select_by_value('search-alias=stripbooks')

#  def hover_lang(self):
# flag = self.find_element()
# actions = ActionChains(self.driver)
# actions.move_to_element(flag)
# actions.perform()

# def select_department(self):
# dropdown = self.find_element(*self.DEPARTMENT_DROPDOWN)
# select = Select(dropdown)
# select.select_by_value('search-alias=stripbooks')

# def verify_cart_count(self,expected_count: str):
#     self.verify_text(expected_count,*self.SHOPCART)

# def verify_spanish_lang_present(self,*FLAG)
# self.wait_for_element_appear()
