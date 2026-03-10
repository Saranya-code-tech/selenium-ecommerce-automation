from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout(driver):
    """
    Verify that a user can successfully complete checkout.
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

    # Start checkout
    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # Enter checkout information
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_checkout_information("John", "Doe", "12345")

    # Continue checkout
    checkout_page.click_continue()

    # Finish order
    checkout_page.click_finish()

    # Verify success message
    success_text = checkout_page.get_success_message()

    assert "Thank you for your order!" in success_text