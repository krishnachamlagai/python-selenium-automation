from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ADD_TO_CART_BUTTON = (By.XPATH, '//button[@data-test="shippingButton"]')
CART_ITEM = (By.XPATH, '//div[data-test="cartItem"]')

@given('Navigate to Given Product Page')
def navigate_to_product_page(context):
    context.driver.get("https://www.target.com/p/juvale-american-flag-fanny-pack-for-women-and-men-patriotic-usa-crossbody-bag-with-adjustable-waist-belt-straps-for-4th-of-july-15-x-5-x-3-in/-/A-79295276")
    sleep(5)


@when('Click on Add To Cart')
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()
    sleep(1)


@given('Navigate to Cart Page')
def navigate_to_cart_page(context):
    context.driver.get("https://www.target.com/cart")
    sleep(5)


@then('Verify given product is present in the cart')
def verify_product_is_present(context):
    cart_items = context.driver.find_elements(*CART_ITEM)
    assert len(cart_items) > 1, f"There are no items in the cart"
