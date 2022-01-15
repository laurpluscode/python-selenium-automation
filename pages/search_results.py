from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResults(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']")
    BOOKS_SUB_NAV = (By.CSS_SELECTOR, "#nav-subnav[data-category='{CATEGORY}']")

    def get_category_locator(self):  # (self,category)
        return [self.SUB[0], self.SUB_NAV[1].replace()]

    # def click_first_product(self,expected_text):
    # self.wait_for_click(*self.SEARCH_RESULT)

    def verify_search_results(self, expected_result):
        actual_result = self.driver.find_element(*self.SEARCH_RESULT).text
        assert actual_result == expected_result, f'Error,actual {actual_result}'

    def verify_search(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)

    def verify_correct_department(self, category):
        locator = self._get_category_locator(category)
        self.wait_for_element_appear(*locator)
