from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_remove_product_from_cart(driver):
    """
    Verify that a product can be removed from the shopping cart.
    """

    # Open website
    driver.get("https://www.saucedemo.com")

    # Login
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # Add product to cart
    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart()

    # Open cart
    inventory_page.open_cart()

    # Remove product
    cart_page = CartPage(driver)
    cart_page.remove_backpack_from_cart()

    # Verify cart is empty
    remaining_items = driver.find_elements(*cart_page.cart_items)

    assert len(remaining_items) == 0