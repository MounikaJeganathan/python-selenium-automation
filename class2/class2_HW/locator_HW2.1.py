from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver_path = ChromeDriverManager().install()

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Amazon logo
driver.find_element(By.XPATH, "//i[@class = 'a-icon a-icon-logo']")

# Email Field
driver.find_element(By.ID, "ap_email")

# continue button
driver.find_element(By.ID, 'continue')
driver.find_element(By.XPATH, "//input[@type = 'submit']")

# need help link
driver.find_element(By.XPATH, "//span[contains(text(),'Need help?')]")
driver.find_element(By.XPATH, "//span[@class = 'a-expander-prompt']")

# Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')
driver.find_element(By.XPATH, "//a[contains(text(),'Forgot your password?')]")

# Other issues with Sign-In link
driver.find_element(By.ID, 'ap-other-signin-issues-link')
driver.find_element(By.XPATH, "//a[contains(text(),'Other issues with Sign-In')]")

# Create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit')
driver.find_element(By.XPATH, "//a[@class = 'a-button-text']")

# *Conditions of use link
driver.find_element(By.XPATH,"//a[@class='a-link-normal'and contains(text(),'Conditions of Use')]")

# *Privacy Notice link
driver.find_element(By.XPATH, "//a[@class = 'a-link-normal' and contains(text(), 'Privacy Notice')]")