from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResults(Page):
    SEARCH_RESULT = (By.XPATH,"//span[@class='a-color-state a-text-bold']")

    def verify_search_results(self,expected_result):
        actual_result = self.driver.find_element(*self.SEARCH_RESULT).text
        assert actual_result == expected_result,f'Error,actual {actual_result}'