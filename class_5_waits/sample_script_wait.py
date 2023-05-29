from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Applied for all find element
# define once
driver.implicitly_wait(4)

# explicit wait
driver.wait = WebDriverWait(driver, 5)

# open the url
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('table')

# wait for 4 sec
# sleep(4)
google_search_btn = (By.NAME, 'btnK')
driver.wait.until(EC.element_to_be_clickable(google_search_btn), message='Google search button is not clickable')

# click search button
driver.find_element(google_search_btn).click()

# verify search results
assert 'table' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

current=driver.current_url
driver.get(current)
driver.quit()
