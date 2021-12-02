from person import Person
from secrets import VENMO_USERNAME, VENMO_PASSWORD
from venmo_api import Client
from typing import List


class Venmo:
    def __init__(self, config: dict):
        """Venmo class to interface with Venmo API

        :param config: global configuration. see config.json
        """
        self.config = config
        self.access_token = Client.get_access_token(username=VENMO_USERNAME, password=VENMO_PASSWORD)
        self.api = Client(access_token=self.access_token)

    def collect(self, people: List[Person]):
        """Collects debt from people through venmo requests

        :param people: list of people to venmo request
        :return: None
        """
        for person in people:
            if person.name not in self.config["phone plan"]["skip"]:
                self.api.payment.request_money(
                    person.debt,
                    self.config["phone plan"]["venmo message"],
                    person.venmo_id
                )

    def logout(self):
        """Logout of Venmo session

        :return: None
        """
        self.api.log_out("Bearer " + self.access_token)
