import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_valid_login(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/login")
        driver.maximize_window()

        driver.find_element(By.ID, "username").send_keys("user123")
        driver.find_element(By.ID, "pwd").send_keys("password")
        driver.find_element(By.ID, "pwd").send_keys(Keys.RETURN)

        time.sleep(2)

        self.assertIn("http://127.0.0.1:5000/", driver.current_url)

    def test_invalid_login(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/login")

        driver.find_element(By.ID, "username").send_keys("123")
        driver.find_element(By.ID, "pwd").send_keys("wrongpassword")
        driver.find_element(By.ID, "pwd").send_keys(Keys.RETURN)

        time.sleep(2)



    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
