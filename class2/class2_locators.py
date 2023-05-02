from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get("https://www.amazon.com/")

# By ID
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.ID, 'nav-search-submit-button')

# By Xpath
driver.find_element(By.XPATH, "//input[@id = 'twotabsearchtextbox']")
driver.find_element(By.XPATH, "//input[@placeholder = 'Search Amazon']")
driver.find_element(By.XPATH, "//*[@placeholder = 'Search Amazon']")


# By Xpath multiple
driver.find_element(By.XPATH, "//input[@name = 'field-keywords' and @aria-label ='Search Amazon']")

# By Xpath with text
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")
driver.find_element(By.XPATH, "//a[contains(@href,'nav_cs_bestsellers')]")
driver.find_element(By.XPATH, "//a[contains(text(),'Best Sellers') and @class = 'nav-a  ']")

# By Xpath with quotation
driver.find_element(By.XPATH, "//img[@alt = \"Mother's day special\"]")

# By XPATH from parent to child
driver.find_element(By.XPATH, "//div[@id = 'nav-xshop-container']//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//div[@id = 'nav-xshop-container']//div[@id = 'nav-xshop']//a[text()='Best Sellers']")
