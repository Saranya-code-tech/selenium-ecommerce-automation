from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Page Object Model for the SauceDemo login page.
    This class contains all locators and actions related to login.
    """

    def __init__(self, driver):
        self.driver = driver

        # Page element locators
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "[data-test='error']")

    def enter_username(self, username):
        """Enter username in the username field"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_input)
        ).send_keys(username)

    def enter_password(self, password):
        """Enter password in the password field"""
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        """Click the login button"""
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        """Complete login workflow"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        """Return login error message text"""
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.error_message)
        ).text