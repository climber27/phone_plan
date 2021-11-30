"""
Purpose: To automate Venmo requesting money for our Verizon phone plan

Notes:
    - Uses Selenium & Chrome. Requires Chrome Selenium driver extension
        - https://sites.google.com/chromium.org/driver/
        - Mac users need to place in /usr/local/bin/ or add the .exec to path
"""
from selenium import webdriver
import time
from parser import Parser
from scraper import Scraper


def main():
    driver = webdriver.Firefox()
    scraper = Scraper(driver)

    # login
    scraper.login()

    # Wait for 2FA
    time.sleep(30)

    # Go to billing
    spans = scraper.get_billing()
    parser = Parser()
    charges = parser.parse_billing_info(spans)
    for charge in charges:
        print(charge)

    # driver.close()


if __name__ == "__main__":
    main()
