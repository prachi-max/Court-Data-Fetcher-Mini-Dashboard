from playwright.sync_api import sync_playwright
import time

def fetch_case_data(case_type, case_number, case_year):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Change to True for headless mode
        page = browser.new_page()

        # Step 1: Open Delhi High Court case status page
        page.goto("https://delhihighcourt.nic.in/app/get-case-type-status")

        # Step 2: Fill in the form
        page.select_option('#case_type', case_type)
        page.fill('#case_number', case_number)
        page.select_option('#case_year', case_year)

        # Step 3: Wait for manual CAPTCHA solving
        input("Please solve the CAPTCHA in the browser, then press Enter here...")

        # Step 4: Click the Submit button (yellow)
        page.click('button.yellow-btn, input[type="submit"]')

        # Wait until button is visible and enabled after solving CAPTCHA
        page.wait_for_selector('button.yellow-btn', state='visible', timeout=60000)

# Now click
        page.click('button.yellow-btn')

        # Step 5: Wait for results table to appear
        # page.wait_for_selector('table', timeout=20000)

        # Step 6: Get HTML of results
        html = page.content()

        # browser.close()
        return html
