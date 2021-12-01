from collections import deque

from person import Person


class Parser:
    def __init__(self, config):
        self.config = config

    @staticmethod
    def parse_billing_info(info):
        charges = deque()
        for elem in info:
            line = elem.text
            if '.' in line and '$' in line and 5 <= len(line) <= 10:
                charges.append(line)

        return charges

    def assign_costs(self, charges):
        people = []
        for user in sorted(self.config["phone plan"]["people"], key=lambda x: x["order"]):
            person = Person(user["name"])
            person.venmo_id = user["venmo id"]
            for _ in user["devices"]:
                charge = float(charges.popleft()[1:])
                person.debt += charge
            people.append(person)

        return people
