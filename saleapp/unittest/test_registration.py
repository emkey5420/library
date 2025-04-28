import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_valid_registration(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/register")
        driver.maximize_window()

        driver.find_element(By.ID, "name").send_keys(" Văn C")
        driver.find_element(By.ID, "username").send_keys("user3") #user chưa tồn tại
        driver.find_element(By.ID, "pwd").send_keys("password")
        driver.find_element(By.ID, "confirm").send_keys("password")

        submit_button = driver.find_element(By.XPATH, "//button[contains(text(),'Đăng ký')]")
        submit_button.click()

        time.sleep(2)

        self.assertIn("http://127.0.0.1:5000/login", driver.current_url)

    def test_username_exists(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/register")


        driver.find_element(By.ID, "name").send_keys("Văn B")
        driver.find_element(By.ID, "username").send_keys("user2")  # Username đã tồn tại
        driver.find_element(By.ID, "pwd").send_keys("password")
        driver.find_element(By.ID, "confirm").send_keys("password")

        submit_button = driver.find_element(By.XPATH, "//button[contains(text(),'Đăng ký')]")
        submit_button.click()

        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
