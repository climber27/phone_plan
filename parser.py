from collections import deque


class Parser:
    def __init__(self):
        pass

    @staticmethod
    def parse_billing_info(info):
        charges = deque()
        for elem in info:
            line = elem.text
            if '.' in line and '$' in line and 5 <= len(line) <= 10:
                charges.append(line)

        return charges
