from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome()

try:
    # Mở trang đăng ký
    driver.get("http://127.0.0.1:5000/register")  # ← URL đăng ký
    driver.maximize_window()

    # Điền thông tin vào form đăng ký
    driver.find_element(By.ID, "name").send_keys("Nguyễn Văn d")  # Tên
    driver.find_element(By.ID, "username").send_keys("d")  # Tên đăng nhập
    driver.find_element(By.ID, "pwd").send_keys("1")  # Mật khẩu
    driver.find_element(By.ID, "confirm").send_keys("1")  # Xác nhận mật khẩu

    # Tìm và nhấn vào nút "Đăng ký" bằng text
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(),'Đăng ký')]")
    submit_button.click()

    # Chờ trang load
    time.sleep(2)

    # Kiểm tra đăng ký thành công và chuyển hướng
    assert "http://127.0.0.1:5000/login" in driver.current_url, "Đăng ký không thành công hoặc không chuyển hướng đúng!"

    print("✅ Đăng ký tài khoản thành công và chuyển hướng tới trang đăng nhập!")

except Exception as e:
    print(f"❌ Có lỗi xảy ra: {e}")

finally:
    # Đóng trình duyệt
    driver.quit()
