import time
import json
import logging
from selenium import webdriver
from parser import Parser
from scraper import Scraper
from person import Person
from venmo import Venmo


def main():
    """Program main function / driver

    Purpose: To automate Venmo requesting money for our Verizon phone plan

    :return: None
    """
    # config
    logging.info("opening config...")
    with open("config.json") as file:
        config = json.load(file)
    logging.info("done")
    logging.info("opening firefox through selenium...")
    driver = webdriver.Firefox()
    logging.info("done")
    scraper = Scraper(driver, config)

    # login
    logging.info("logging into Verizon's website...")
    scraper.login()
    logging.info("done")

    # Wait for 2FA
    logging.info("waiting on 2FA...")
    time.sleep(config["phone plan"]["2FA time"])
    logging.info("done")

    # Go to billing
    logging.info("redirect to billing...")
    spans = scraper.get_billing()
    logging.info("done")
    logging.info("parsing charges...")
    parser = Parser(config)
    charges = parser.parse_billing_info(spans)
    logging.info("done")

    # Assign costs
    logging.info("assigning costs...")
    people = parser.assign_costs(charges)
    logging.info("done")

    # charge
    logging.info("Sending out Venmos...")
    venmo = Venmo(config)
    venmo.collect(people=people)
    venmo.logout()
    logging.info("done")

    # driver.close()


if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)
    main()
