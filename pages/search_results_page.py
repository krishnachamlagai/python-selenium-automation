from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT_HEADING_TEXT = (By.XPATH, "//div[@data-test='resultsHeading']")

    def verify_search_results(self, expected_text):
        actual_text = self.find_element(*self.SEARCH_RESULT_HEADING_TEXT).text
        assert expected_text in actual_text, f'Error! Text {expected_text} not in {actual_text}'

