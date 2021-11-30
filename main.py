"""
Purpose: To automate Venmo requesting money for our Verizon phone plan

Notes:
    - Uses Selenium & Chrome. Requires Chrome Selenium driver extension
        - https://sites.google.com/chromium.org/driver/
        - Mac users need to place in /usr/local/bin/ or add the .exec to path
"""
import time
import json
from selenium import webdriver
from parser import Parser
from scraper import Scraper
from person import Person


def main():
    # config
    with open("./people.json") as file:
        config = json.load(file)

    driver = webdriver.Firefox()
    scraper = Scraper(driver)

    # login
    scraper.login()

    # Wait for 2FA
    time.sleep(config["phone plan"]["2FA time"])

    # Go to billing
    spans = scraper.get_billing()
    parser = Parser()
    charges = parser.parse_billing_info(spans)

    # Assign costs
    people = []
    for user in sorted(config["phone plan"]["people"], key=lambda x: x["order"]):
        person = Person(user["name"])
        for _ in user["devices"]:
            charge = float(charges.popleft()[1:])
            person.debt += charge
        people.append(person)

    total = 0.0
    for p in people:
        total += p.debt
        print("name: {}, debt: {}".format(p.name, p.debt))

    print("TOTAL: {}".format(total))

    # driver.close()


if __name__ == "__main__":
    main()
