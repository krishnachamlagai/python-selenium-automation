from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from behave import given, when, then

CART_EMPTY_HEADING = (By.XPATH, "//h1[contains(text(), 'Your cart is empty')]")


@given('Open Target main page')
def open_target_page(context):
    context.driver.get("https://www.target.com/")


@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.XPATH, "//a[@href='/cart?prehydrateClick=true']").click()


@then('Your cart is empty message is shown')
def verify_cart_is_empty(context):
    context.wait.until(ec.presence_of_element_located(CART_EMPTY_HEADING))
    cart_empty_text_h1 = context.driver.find_element(CART_EMPTY_HEADING)
    assert cart_empty_text_h1 is not None

