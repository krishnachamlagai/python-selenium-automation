from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import Page


class AddToCart(Page):
    ADD_TO_CART_BUTTON = (By.XPATH, '//button[@data-test="orderPickupButton"]')
    ADD_TO_CART_BUTTON2 = (By.CSS_SELECTOR, 'button[data-test="shippingButton"][aria-label*="Add to cart"]')
    CART_ITEM = (By.XPATH, '//div[data-test="cartItem"]')

    def navigate_to_product_page(self, product_id):
        self.driver.get(f"https://www.target.com/p/{product_id}")

    def navigate_to_cart_page(self):
        self.driver.get("https://www.target.com/cart")

    def click_add_to_cart(self):
        # self.wait.until(ec.visibility_of_element_located(self.ADD_TO_CART_BUTTON))
        self.click(*self.ADD_TO_CART_BUTTON2)

    def verify_product_is_present(self):
        # self.wait.until(ec.presence_of_element_located(self.CART_ITEM))
        cart_items = self.find_elements(*self.CART_ITEM)
        assert len(cart_items) > 1, f"There are no items in the cart"




