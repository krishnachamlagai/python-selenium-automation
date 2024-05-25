from behave import given, when, then


@given('Navigate to Given Product Page {product_id}')
def navigate_to_product_page(context, product_id):
    context.app.add_to_cart_page.navigate_to_product_page(product_id)


@when('Click on Add To Cart')
def add_to_cart(context):
    context.app.add_to_cart_page.click_add_to_cart()


@given('Navigate to Cart Page')
def navigate_to_cart_page(context):
    context.app.add_to_cart_page.navigate_to_cart_page()


@then('Verify given product is present in the cart')
def verify_product_is_present(context):
    context.app.add_to_cart_page.verify_product_is_present()
