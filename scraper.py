from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from secrets import *


class Scraper:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.get("https://www.verizonwireless.com/my-verizon/")
        try:
            user = WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located((By.NAME, "IDToken1"))
            )
            user.clear()
            user.send_keys(VERIZON_USERNAME)
            password = self.driver.find_element(By.NAME, "IDToken2")
            password.send_keys(VERIZON_PASSWORD)
            self.driver.find_element(By.ID, "login-submit").click()
        except Exception as e:
            print(e)

    def get_billing(self):
        self.driver.get("https://www.verizon.com/digital/nsa/secure/ui/bill/viewbill/")
        time.sleep(5)
        info = self.driver.find_elements(By.TAG_NAME, "span")

        return info
