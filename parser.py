from collections import deque
from typing import List
from selenium.webdriver.remote.webelement import WebElement
from person import Person


class Parser:
    def __init__(self, config: dict):
        """Parser class to consumer scraped output
        Currently only parses Verizon scraped output
        :param config:
        """
        self.config = config

    @staticmethod
    def parse_billing_info(info: List[WebElement]) -> deque:
        """Parses billing html
        :param info: billing html
        :return: queue of floats
        """
        charges = deque()
        for elem in info:
            line = elem.text
            if '.' in line and '$' in line and 5 <= len(line) <= 10:
                charges.append(float(line[:1]))  # removes $ and casts str to float

        return charges

    def assign_costs(self, charges: deque) -> List[Person]:
        """Assigns debt to people
        :param charges: queue of floats
        :return: list of people with debt
        """
        people = []
        for obj in sorted(self.config["phone plan"]["people"], key=lambda x: x["order"]):
            person = Person(obj["name"])
            person.venmo_id = obj["venmo id"]
            for _ in obj["devices"]:
                person.debt += charges.popleft()
            people.append(person)

        # log
        total = 0.0
        for p in people:
            total += p.debt
            print("name: {}, debt: {}".format(p.name, p.debt))

        print("TOTAL: {}".format(total))

        if total > 235:
            raise AssertionError("Please double check cost")

        return people
