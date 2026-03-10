from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_product_to_cart(driver):
    """
    Verify that a product can be added to the shopping cart.
    """

    # Open website
    driver.get("https://www.saucedemo.com")

    # Login
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # Add product to cart
    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart()

    # Navigate to cart
    inventory_page.open_cart()

    # Verify product appears in cart
    cart_page = CartPage(driver)
    cart_items = cart_page.get_cart_items()

    assert "Sauce Labs Backpack" in cart_items