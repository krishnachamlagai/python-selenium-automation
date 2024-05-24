from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from behave import given, when, then

PRODUCT_COLORS_IMG = (By.CSS_SELECTOR, "[class*='StyledBaseButtonInternal'] img")
PRODUCT_COLOR_TEXT = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='StyledHeaderWrapperDiv']")


@given('Open Target Product {product_id}')
def open_target_product(context, product_id):
    context.driver.get("https://www.target.com/p/{0}".format(product_id))


@then('Verify user can click through colors')
def verify_colors(context):
    available_product_colors = []
    selected_product_colors = []
    context.wait.until(ec.visibility_of_element_located(PRODUCT_COLORS_IMG))
    product_colors = context.driver.find_elements(*PRODUCT_COLORS_IMG)

    for product in product_colors:
        product_color = product.get_attribute("alt")
        available_product_colors.append(product_color)
        product.click()
        context.wait.until(ec.presence_of_element_located(PRODUCT_COLOR_TEXT))
        selected_color_value = context.driver.find_element(*PRODUCT_COLOR_TEXT).text
        selected_color_value = selected_color_value.split('\n')[1]
        selected_product_colors.append(selected_color_value)

    assert available_product_colors == selected_product_colors, f"All colors {available_product_colors} are different in {selected_product_colors}"



