from collections import deque

from person import Person


class Parser:
    def __init__(self, config):
        """

        :param config:
        """
        self.config = config

    @staticmethod
    def parse_billing_info(info):
        """

        :param info:
        :return:
        """
        charges = deque()
        for elem in info:
            line = elem.text
            if '.' in line and '$' in line and 5 <= len(line) <= 10:
                charges.append(line)

        return charges

    def assign_costs(self, charges):
        """

        :param charges:
        :return:
        """
        people = []
        for obj in sorted(self.config["phone plan"]["people"], key=lambda x: x["order"]):
            person = Person(obj["name"])
            person.venmo_id = obj["venmo id"]
            for _ in obj["devices"]:
                person.debt += float(charges.popleft()[1:])
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
