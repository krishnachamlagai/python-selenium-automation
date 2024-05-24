from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from behave import given, when, then

SIGN_IN_BUTTON = (By.XPATH, "//a[@aria-label='Account, sign in']")
SIGN_IN_AGAIN_LINK = (By.XPATH, "//a[@data-test='accountNav-signIn']")
SIGN_IN_TEXT = (By.XPATH, "//span[contains(text(), 'Sign into your Target account')]")


@when('click sign in')
def click_sign_in(context):
    context.wait.until(ec.visibility_of_element_located(SIGN_IN_BUTTON))
    context.driver.find_element(*SIGN_IN_BUTTON).click()


@when('click Sign In after it opens right side navigation menu')
def click_sign_in_again(context):
    context.wait.until(ec.presence_of_element_located(SIGN_IN_AGAIN_LINK))
    context.driver.find_element(*SIGN_IN_AGAIN_LINK).click()


@then('sign In form opens')
def verify_sign_in_form(context):
    context.wait.until(ec.visibility_of_element_located(SIGN_IN_TEXT))
    signin_form_heading_txt = context.driver.find_element(*SIGN_IN_TEXT)
    assert signin_form_heading_txt is not None



