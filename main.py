"""
Purpose: To automate Venmo requesting money for our Verizon phone plan

Notes:
    - Uses Selenium & Chrome. Requires Chrome Selenium driver extension
        - https://sites.google.com/chromium.org/driver/
        - Mac users need to place in /usr/local/bin/ or add the .exec to path
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from secrets import *


def main():
    driver = webdriver.Chrome()
    driver.get("https://www.verizonwireless.com/my-verizon/")
    try:
        user = WebDriverWait(driver, 25).until(
            EC.presence_of_element_located((By.NAME, "IDToken1"))
        )
        user.clear()
        user.send_keys(VERIZON_USERNAME)
        password = driver.find_element(By.NAME, "IDToken2")
        password.send_keys(VERIZON_PASSWORD)
        driver.find_element(By.ID, "login-submit").click()
    except Exception as e:
        print(e)

    # driver.close()


if __name__ == "__main__":
    main()
