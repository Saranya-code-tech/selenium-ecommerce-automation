# Selenium E-Commerce Automation Framework

This project is a UI automation framework built using **Python, Selenium WebDriver, and PyTest** for testing the SauceDemo e-commerce website.

## Features Covered

- Open website validation
- Valid login test
- Invalid login test
- Add product to cart
- Remove product from cart
- End-to-end checkout flow

## Framework Design

- Page Object Model (POM)
- PyTest fixtures for browser setup and teardown
- Explicit waits using WebDriverWait
- Failure screenshots for debugging
- HTML test reports

## Tech Stack

- Python
- Selenium WebDriver
- PyTest
- WebDriver Manager
- PyTest HTML Report

## Project Structure

```bash
selenium-ecommerce-automation/
│
├── pages/
├── tests/
├── utilities/
├── reports/
├── screenshots/
├── requirements.txt
├── README.md
└── .gitignore