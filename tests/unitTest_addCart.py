import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):

        driver = self.driver
        driver.maximize_window()
        user = "testuser"
        pwd = "test123456!"
        driver.get("http://127.0.0.1:8000/accounts/login/")
        time.sleep(3)
        elem = driver.find_element(By.ID,"id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID,"id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)

        driver.find_element(By.XPATH, "//a[contains(., 'Menu')]").click()

        driver.find_element(By.XPATH, "//a[contains(., 'Cake')]").click()

        driver.find_element(By.XPATH, "//a[contains(., 'Strawberry Shortcake')]").click()

        driver.find_element(By.XPATH, "//input[@value='Add to cart']").click()

        time.sleep(5)
        try:
            self.driver.close()
            assert True

        except NoSuchElementException:
            driver.close()
            self.fail("Could not add item to cart")

        time.sleep(5)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()