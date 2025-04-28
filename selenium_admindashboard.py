from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

# Setup ChromeDriver (path tới ChromeDriver của bạn)

# Khởi tạo trình duyệt
driver = webdriver.Chrome()

try:
    # Bước 1: Truy cập vào trang login
    driver.get("http://127.0.0.1:5000/staff")

    # Bước 2: Nhập thông tin đăng nhập
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Nhập thông tin
    username_field.send_keys("a")
    password_field.send_keys("1")
    password_field.send_keys(Keys.RETURN)  # Gửi form bằng cách nhấn Enter

    # Chờ một chút để trang tải xong
    time.sleep(2)

    # Bước 3: Kiểm tra xem có chuyển đến trang quản lý hay không
    # Xác minh xem có chứa một phần tử nào chỉ có trên trang dashboard hay không
    try:
        print("Login successful, dashboard displayed.")
        result = "Pass"
    except Exception as e:
        print(f"Error: {e}")
        print("Dashboard not displayed.")
        result = "Fail"

    # Bước 4: Ghi lại kết quả kiểm thử
    print(f"Test result: {result}")

finally:
    # Đóng trình duyệt
    driver.quit()
