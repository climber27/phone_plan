from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from secrets import *


class Scraper:
    def __init__(self, driver, config):
        """Class to interface with Selenium web scraper
        Currently, this is only used to get billing info from Verizon
        :param driver: selenium driver
        :param config: global configuration. see config.json
        """
        self.driver = driver
        self.config = config

    def login(self):
        """Login to Verizon
        The page does a number of things to load, so this waits for the login for to show up
        :return: None
        """
        self.driver.get(self.config["phone plan"]["login url"])
        try:
            user = WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located((By.NAME, self.config["phone plan"]["username element"]))
            )
            user.clear()
            user.send_keys(VERIZON_USERNAME)
            password = self.driver.find_element(By.NAME, self.config["phone plan"]["password element"])
            password.send_keys(VERIZON_PASSWORD)
            self.driver.find_element(By.ID, self.config["phone plan"]["login element"]).click()
        except Exception as e:
            print(e)

    def get_billing(self) -> List[WebElement]:
        """Gets billing info from Verizon
        Grabs all elements where billing info might be. The parser then consumes this output
        :return: List[WebElement]
        """
        self.driver.get(self.config["phone plan"]["billing url"])
        # wait for page to load
        time.sleep(5)
        info = self.driver.find_elements(By.TAG_NAME, self.config["phone plan"]["billing element"])

        return info
