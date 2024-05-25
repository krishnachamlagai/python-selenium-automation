from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_INPUT = (By.ID, "search")
    SEARCH_BUTTON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    def search_product(self, search_keyword):
        self.input_text(search_keyword, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BUTTON)
