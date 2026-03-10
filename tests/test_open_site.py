def test_open_site(driver):
    """
    Verify that the SauceDemo website loads successfully.
    """

    # Open the website
    driver.get("https://www.saucedemo.com")

    # Verify the page title contains "Swag Labs"
    assert "Swag Labs" in driver.title