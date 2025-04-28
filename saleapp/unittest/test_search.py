import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_book_found(self): #tìm kiếm sách có trong trang web
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")  # URL trang chủ
        driver.maximize_window()

        # Tìm ô input tìm kiếm và nhập từ khóa tìm kiếm
        search_box = driver.find_element(By.NAME, "kw")  # Tìm kiếm theo trường "kw" trong header.html
        search_box.send_keys("bà")  # Từ khóa tìm kiếm "Python"
        search_box.send_keys(Keys.RETURN)  # Nhấn Enter để tìm kiếm

        # Đợi kết quả tìm kiếm xuất hiện
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "row"))  # Chờ đến khi danh sách sách được hiển thị
        )

        # Kiểm tra xem có sách liên quan đến "Python" không
        books = driver.find_elements(By.CLASS_NAME, "card")  # Lấy tất cả thẻ card đại diện cho sách
        found = False
        for book in books:
            if "bà" in book.text:
                found = True
                break



    def test_search_book_not_found(self): #tìm kiếm sách không có trong trang web
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")  # URL trang chủ
        driver.maximize_window()

        # Tìm ô input tìm kiếm và nhập từ khóa tìm kiếm
        search_box = driver.find_element(By.NAME, "kw")  # Tìm kiếm theo trường "kw" trong header.html
        search_box.send_keys("abcdef")  # Từ khóa tìm kiếm không tồn tại "abcdef"
        search_box.send_keys(Keys.RETURN)  # Nhấn Enter để tìm kiếm

        # Đợi kết quả tìm kiếm xuất hiện
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "row"))  # Chờ đến khi danh sách sách được hiển thị
        )

        # Kiểm tra xem có thông báo "KHÔNG có sách nào" hoặc danh sách sách rỗng

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
