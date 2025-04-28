from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

# Khởi tạo trình duyệt
driver = webdriver.Chrome()

# Đăng nhập vào hệ thống
driver.get("http://127.0.0.1:5000/login")  # Truy cập trang đăng nhập

# Tìm input username và nhập giá trị
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("kha")  # ← Username mới

# Tìm input password và nhập giá trị
password_input = driver.find_element(By.ID, "pwd")
password_input.send_keys("1")  # ← Password mới

# Submit form
password_input.send_keys(Keys.RETURN)

# Chờ đăng nhập
time.sleep(2)

# Truy cập trang chi tiết sách sau khi đăng nhập
driver.get("http://127.0.0.1:5000/books/1")  # Thay ID sách nếu cần

# Nhập bình luận vào ô textarea
comment_box = driver.find_element(By.ID, "comment")
comment_box.send_keys("Bình luận thử qua Selenium.")

# Gửi bình luận
comment_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Bình luận')]")
comment_button.click()

# Chờ bình luận được thêm vào
time.sleep(2)

# Kiểm tra xem bình luận đã hiển thị chưa
try:
    new_comment = driver.find_element(By.XPATH,
                                      "//ul[@id='comments']//li[contains(text(), 'Bình luận thử qua Selenium')]")
    print("Bình luận đã được thêm thành công và hiển thị!")
except Exception as e:
    print(f"Bình luận không hiển thị: {e}")

# Đóng trình duyệt sau khi kiểm thử
driver.quit()
