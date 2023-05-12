from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service= Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get("https://www.amazon.com/")

# By ID
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')
driver.find_element(By.ID, 'nav-search-submit-button').click()

expected_result = '"table"'
actual_result = driver.find_element(By.XPATH, "//span[@class = 'a-color-state a-text-bold']").text
assert expected_result == actual_result, f'Error !! Actual result {actual_result} is not equal to expected result/' \
                                         f'{expected_result}'

print("Test case is passed")


driver.quit()
