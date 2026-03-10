from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    Page Object Model for the cart page.
    Handles removing products and proceeding to checkout.
    """

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.cart_items = (By.CLASS_NAME, "inventory_item_name")
        self.remove_backpack_button = (By.ID, "remove-sauce-labs-backpack")
        self.checkout_button = (By.ID, "checkout")

    def get_cart_items(self):
        """Return a list of product names currently in the cart"""
        elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.cart_items)
        )
        return [element.text for element in elements]

    def remove_backpack_from_cart(self):
        """Remove backpack item from cart"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.remove_backpack_button)
        ).click()

    def click_checkout(self):
        """Click checkout button to start purchase process"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()