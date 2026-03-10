from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    Page Object Model for checkout process.
    Handles entering user details and completing purchase.
    """

    def __init__(self, driver):
        self.driver = driver

        # Checkout form locators
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.success_message = (By.CLASS_NAME, "complete-header")

    def enter_checkout_information(self, first_name, last_name, postal_code):
        """Fill checkout form fields"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.first_name_input)
        ).send_keys(first_name)

        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)

    def click_continue(self):
        """Continue to order summary page"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()

    def click_finish(self):
        """Finish purchase"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.finish_button)
        ).click()

    def get_success_message(self):
        """Return order confirmation message"""
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.success_message)
        ).text