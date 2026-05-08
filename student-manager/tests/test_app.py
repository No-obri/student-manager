import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

BASE_URL = "http://app:5000"

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")
    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()

def test_page_title(driver):
    """Test Case 1: Verify page loads with correct title"""
    driver.get(BASE_URL)
    assert "Student Manager" in driver.title, f"Expected 'Student Manager' in title, got: {driver.title}"
    print("PASS: Page title verified")

def test_add_student(driver):
    """Test Case 2: Verify a student can be added via the form"""
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)

    name_input = wait.until(EC.presence_of_element_located((By.NAME, "name")))
    grade_input = driver.find_element(By.NAME, "grade")

    name_input.clear()
    name_input.send_keys("Ali Ahmed")
    grade_input.clear()
    grade_input.send_keys("A+")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)

    page_source = driver.page_source
    assert "Ali Ahmed" in page_source, "Student name not found in page after adding"
    print("PASS: Student added and displayed correctly")
