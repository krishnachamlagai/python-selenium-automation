from selenium.webdriver.common.by import By
from pages.base_page import Page


class LoginPage(Page):
    LINK_XPATH = (By.XPATH, "//a[text()='Target terms and conditions']")

    def click_on_target_tac_link(self):
        self.find_element(*self.LINK_XPATH).click()



