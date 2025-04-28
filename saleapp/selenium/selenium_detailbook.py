from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome()

# Mở trang chủ
driver.get("http://127.0.0.1:5000/")

# Tìm liên kết đến sách (Giả sử bạn có các liên kết sách trên trang chủ)
book_link = driver.find_element(By.XPATH, "//a[contains(@href, '/books/')]")  # Tìm liên kết sách
book_link.click()

# Chờ trang chi tiết sách tải
time.sleep(2)

# Kiểm tra xem chi tiết sách và phần bình luận có hiển thị không
try:
    book_name = driver.find_element(By.TAG_NAME, "h1")
    book_price = driver.find_element(By.CLASS_NAME, "text-danger")
    comments_section = driver.find_element(By.ID, "comments")
    print("Kiểm tra chi tiết sách thành công: Hiển thị chi tiết sách và bình luận")
except Exception as e:
    print(f"Kiểm tra chi tiết sách thất bại: {e}")

# Đóng trình duyệt sau khi kiểm thử
driver.quit()
