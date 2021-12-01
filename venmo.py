from person import Person
from secrets import VENMO_USERNAME, VENMO_PASSWORD
from venmo_api import Client
from typing import List


class Venmo:
    def __init__(self, config: dict):
        """

        :param config:
        """
        self.config = config
        self.access_token = Client.get_access_token(username=VENMO_USERNAME, password=VENMO_PASSWORD)
        self.api = Client(access_token=self.access_token)

    def collect(self, people: List[Person]):
        """

        :param people:
        :return:
        """
        for person in people:
            if person not in self.config["phone plan"]["skip"]:
                self.api.payment.request_money(person.debt, "Verizon Phone Bill", person.venmo_id)

    def logout(self):
        """

        :return:
        """
        self.api.log_out("Bearer " + self.access_token)
