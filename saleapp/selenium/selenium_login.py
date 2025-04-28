from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome()

try:
    # Mở trang login
    driver.get("http://127.0.0.1:5000/login")  # ← URL mới
    driver.maximize_window()

    # Tìm input username và nhập giá trị
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("kha")  # ← Username mới

    # Tìm input password và nhập giá trị
    password_input = driver.find_element(By.ID, "pwd")
    password_input.send_keys("1")    # ← Password mới

    # Submit form
    password_input.send_keys(Keys.RETURN)

    # Chờ trang load
    time.sleep(2)

    # Kiểm tra xem đăng nhập thành công chưa
    assert "http://127.0.0.1:5000/" in driver.current_url, "Login failed or not redirected to homepage!"

    print("✅ Test đăng nhập thành công!")

except Exception as e:
    print(f"❌ Có lỗi xảy ra: {e}")

finally:
    # Đóng trình duyệt
    driver.quit()
