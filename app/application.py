from pages.header import Header
from pages.main_page import MainPage


# from pages.search_results_page import  SearchResults

def SearchResults():
    pass


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.header = Header(self)
        self.main_page = MainPage(self.driver)
    # self.search_results = SearchResults()
