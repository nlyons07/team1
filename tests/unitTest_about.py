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
        driver.get("http://127.0.0.1:8000/admin")

        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID, "id_password")
        elem.send_keys(pwd)

        elem.send_keys(Keys.RETURN)
        #time.sleep(10)
        driver.get("http://127.0.0.1:8000/about/")
        time.sleep(5)

        # find 'about' and click it – note this is all one Python statement
        #driver.find_element(By.XPATH, "//a[contains(., 'All Books')]").click()


        try:
            # verify about page exists on new screen after clicking "About" button

            #//*[@id="navBar"]/div[1]/a[2]
            #/html/body/div[1]/div[1]/a[2]- full x path

            elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/a[2]")
            self.driver.close()
            assert True
        except NoSuchElementException:
            driver.close()
            self.fail("About page does not appear when About is clicked")


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
