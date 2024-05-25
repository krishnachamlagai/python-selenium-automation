from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from pages.target_app_page import TargetAppPage
from pages.login_page import LoginPage
from pages.add_to_cart import AddToCart


class Application:
    def __init__(self, driver):
        self.add_to_cart_page = AddToCart(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.target_app_page = TargetAppPage(driver)
