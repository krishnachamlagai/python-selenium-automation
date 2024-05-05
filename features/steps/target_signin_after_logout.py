from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# @given('open Target main page')
# def open_target_page(context):
#     context.driver.get("https://www.target.com/")


@when('click sign in')
def click_sign_in(context):
    signin_button = context.driver.find_element(By.XPATH, "//a[@aria-label='Account, sign in']")
    signin_button.click()
    sleep(3)


@when('click Sign In after it opens right side navigation menu')
def click_sign_in_again(context):
    signin_button = context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']")
    signin_button.click()
    sleep(5)


@then('sign In form opens')
def verify_sign_in_form(context):
    signin_form_heading_txt = context.driver.find_element(By.XPATH, "//span[contains(text(), 'Sign into your Target account')]")
    assert signin_form_heading_txt is not None



