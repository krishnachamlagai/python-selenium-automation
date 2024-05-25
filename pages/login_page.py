from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import Page


class LoginPage(Page):
    SIGN_IN_BUTTON = (By.XPATH, "//a[@aria-label='Account, sign in']")
    SIGN_IN_AGAIN_LINK = (By.XPATH, "//a[@data-test='accountNav-signIn']")
    SIGN_IN_TEXT = (By.XPATH, "//span[contains(text(), 'Sign into your Target account')]")
    LINK_XPATH = (By.XPATH, "//a[text()='Target terms and conditions']")

    def click_sign_in(self):
        self.wait.until(ec.visibility_of_element_located(self.SIGN_IN_BUTTON))
        self.click(*self.SIGN_IN_BUTTON)

    def click_sign_in_again(self):
        self.wait.until(ec.presence_of_element_located(self.SIGN_IN_AGAIN_LINK))
        self.click(*self.SIGN_IN_AGAIN_LINK)

    def verify_sign_in_form(self):
        self.wait.until(ec.visibility_of_element_located(self.SIGN_IN_TEXT))
        return self.find_element(*self.SIGN_IN_TEXT)

    def click_on_target_tac_link(self):
        self.find_element(*self.LINK_XPATH).click()



