import os
import pytest
from datetime import datetime
from utilities.driver_setup import get_driver


@pytest.fixture
def driver():
    """
    Initialize browser before each test and quit after test.
    """
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    PyTest hook to capture test result.
    If a test fails, save a screenshot in the screenshots folder.
    """
    outcome = yield
    report = outcome.get_result()

    # Only take screenshot if test actually failed during test execution
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            test_name = item.name
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_file = os.path.join(
                screenshots_dir, f"{test_name}_{timestamp}.png"
            )

            driver.save_screenshot(screenshot_file)
            print(f"\nScreenshot saved: {screenshot_file}")