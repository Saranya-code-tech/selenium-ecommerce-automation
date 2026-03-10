# Selenium E-Commerce Automation Framework

This project is a UI test automation framework built using **Python, Selenium WebDriver, and PyTest** for testing the SauceDemo e-commerce website.

## Features Automated

- Open website validation
- Valid login
- Invalid login validation
- Add product to cart
- Remove product from cart
- End-to-end checkout workflow

## Framework Design

This automation framework follows:

- Page Object Model (POM)
- PyTest fixtures for browser setup
- Explicit waits using WebDriverWait
- HTML test reporting
- Screenshot capture on test failures

## Technologies Used

- Python
- Selenium WebDriver
- PyTest
- WebDriver Manager
- PyTest HTML Reports

## Project Structure
selenium-ecommerce-automation/
│
├── pages/
├── tests/
├── utilities/
├── reports/
├── screenshots/
├── requirements.txt
└── README.md


## How to Run Tests

Install dependencies:
pip install -r requirements.txt

Run tests:
pytest tests -v

Run tests with HTML report:
pytest tests -v --html=reports/report.html --self-contained-html

## Test Website

Website used for automation testing:

https://www.saucedemo.com

Credentials:

Username: standard_user  
Password: secret_sauce

## Author

Saranya Ethiraj
