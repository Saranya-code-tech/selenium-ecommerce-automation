from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """
    Page Object Model for the product inventory page.
    Handles actions like adding items to the cart.
    """

    def __init__(self, driver):
        self.driver = driver

        # Element locators
        self.add_backpack_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart(self):
        """Click 'Add to Cart' button for the backpack"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_backpack_button)
        ).click()

    def open_cart(self):
        """Click the cart icon to navigate to cart page"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_icon)
        ).click()