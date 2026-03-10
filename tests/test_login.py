from pages.login_page import LoginPage


def test_valid_login(driver):
    """
    Verify that a user can log in with valid credentials.
    """

    # Open login page
    driver.get("https://www.saucedemo.com")

    # Perform login
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # Verify successful login by checking URL
    assert "inventory" in driver.current_url


def test_invalid_login(driver):
    """
    Verify that an error message appears when login fails.
    """

    # Open login page
    driver.get("https://www.saucedemo.com")

    # Attempt login with incorrect credentials
    login_page = LoginPage(driver)
    login_page.login("wrong_user", "wrong_password")

    # Capture the error message
    error_text = login_page.get_error_message()

    # Verify correct error message appears
    assert "Username and password do not match" in error_text