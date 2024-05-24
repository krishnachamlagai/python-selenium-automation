from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from behave import given, when, then


ADD_TO_CART_BUTTON = (By.XPATH, '//button[@data-test="shippingButton"]')
CART_ITEM = (By.XPATH, '//div[data-test="cartItem"]')


@given('Navigate to Given Product Page')
def navigate_to_product_page(context):
    context.driver.get("https://www.target.com/p/juvale-american-flag-fanny-pack-for-women-and-men-patriotic-usa-crossbody-bag-with-adjustable-waist-belt-straps-for-4th-of-july-15-x-5-x-3-in/-/A-79295276")


@when('Click on Add To Cart')
def add_to_cart(context):
    context.wait.until(ec.element_to_be_clickable(ADD_TO_CART_BUTTON))
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()


@given('Navigate to Cart Page')
def navigate_to_cart_page(context):
    context.driver.get("https://www.target.com/cart")


@then('Verify given product is present in the cart')
def verify_product_is_present(context):
    context.wait.until(ec.presence_of_element_located(CART_ITEM))
    cart_items = context.driver.find_elements(*CART_ITEM)
    assert len(cart_items) > 1, f"There are no items in the cart"
