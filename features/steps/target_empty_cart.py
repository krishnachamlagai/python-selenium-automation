from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target_page(context):
    context.driver.get("https://www.target.com/")


@when('Click on Cart icon')
def click_cart_icon(context):
    cart_icon = context.driver.find_element(By.XPATH, "//a[@href='/cart?prehydrateClick=true']")
    cart_icon.click()
    sleep(5)


@then('Your cart is empty message is shown')
def verify_cart_is_empty(context):
    cart_empty_text_h1 = context.driver.find_element(By.XPATH, "//h1[contains(text(), 'Your cart is empty')]")
    assert cart_empty_text_h1 is not None

