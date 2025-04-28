import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestCartOperations(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_add_to_cart(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/books/1")  # Giả sử ID sách là 1
        driver.maximize_window()

        add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(),'Đặt hàng')]")
        add_to_cart_button.click()

        time.sleep(2)

        cart_link = driver.find_element(By.ID, "cart-link")
        cart_link.click()
        time.sleep(2)

        cart_item = driver.find_element(By.XPATH, "//td[contains(text(),'Python')]")  # Giả sử tên sách là 'Python'
        self.assertIsNotNone(cart_item)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
