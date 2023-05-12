from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver_path = ChromeDriverManager().install()

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Test Case: Logged out user sees Sign in page when clicking Orders

driver.get("https://www.amazon.com/")

# clicking orders
driver.find_element(By.XPATH, "//a[@id ='nav-orders']//span[@class ='nav-line-2']").click()

# opens sign in page and verify sign in header is visible

assert driver.find_element(By.XPATH, "//h1[@class = 'a-spacing-small' and contains(text(),'Sign in')]").is_displayed(), \
    f'Error!!, Sign In header is not displayed '

print("Sign in Page loaded sucessfully ")

# verifies email field is present

assert driver.find_element(By.ID, 'ap_email').is_displayed(), f'Error!! Email field is not displayed '

print("Email field is displayed")

driver.quit()
