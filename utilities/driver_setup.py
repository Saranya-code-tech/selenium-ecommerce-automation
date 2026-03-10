from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    """
    This function initializes the Chrome browser for our tests.
    It disables password popups and runs the browser in incognito mode
    so every test starts with a clean session.
    """

    options = Options()

    # Run browser in incognito mode to avoid cached data
    options.add_argument("--incognito")

    # Disable browser notifications
    options.add_argument("--disable-notifications")

    # Disable Chrome password manager popup
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    # Automatically download and start the correct ChromeDriver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    # Maximize browser window for better visibility
    driver.maximize_window()

    # Ensure no previous cookies interfere with tests
    driver.delete_all_cookies()

    return driver