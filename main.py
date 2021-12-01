import time
import json
from selenium import webdriver
from parser import Parser
from scraper import Scraper
from person import Person


def main():
    """Program main function / driver

    Purpose: To automate Venmo requesting money for our Verizon phone plan

    :return: None
    """
    # config
    with open("config.json") as file:
        config = json.load(file)

    driver = webdriver.Firefox()
    scraper = Scraper(driver)

    # login
    scraper.login()

    # Wait for 2FA
    time.sleep(config["phone plan"]["2FA time"])

    # Go to billing
    spans = scraper.get_billing()
    parser = Parser(config)
    charges = parser.parse_billing_info(spans)

    # Assign costs
    people = parser.assign_costs(charges)

    # driver.close()


if __name__ == "__main__":
    main()
