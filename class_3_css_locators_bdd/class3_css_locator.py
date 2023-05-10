from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# By ID with CSS selector(use #)(use $$ in console)

driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')

# By class with CSS selector(use .)

driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag')
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag.icp-nav-flag-us')
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag.icp-nav-flag-us.icp-nav-flag-lop')
driver.find_element(By.CSS_SELECTOR, '.icp-nav-flag.icp-nav-flag-us.icp-nav-flag-lop')

# Mix with id and class - order does not matter , but prefering id to be first

driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox.nav-input')
driver.find_element(By.CSS_SELECTOR, '.nav-input#twotabsearchtextbox')

# By CSS, attributes:
driver.find_element(By.CSS_SELECTOR,
                    "a[href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")
# By CSS, attributes, partial match: *=
driver.find_element(By.CSS_SELECTOR, "a[href*='ref=ap_signin_notification_condition_of_use?']")

# Multiple attributes:
driver.find_element(By.CSS_SELECTOR, "a[data-csa-c-func-deps='aui-da-a-expander-toggle'][role='button']")
driver.find_element(By.CSS_SELECTOR, "[data-csa-c-func-deps='aui-da-a-expander-toggle'][role='button']")

# CSS with class and attribute :
driver.find_element(By.CSS_SELECTOR,
                    "a.a-expander-header[data-csa-c-func-deps='aui-da-a-expander-toggle'][role='button']")
driver.find_element(By.CSS_SELECTOR,
                    ".a-expander-header[data-csa-c-func-deps='aui-da-a-expander-toggle'][role='button']")


# From parent to child:(multiple tags separted with space)

driver.find_element(By.CSS_SELECTOR, "#legalTextRow a[href*='condition_of_use']")
driver.find_element(By.CSS_SELECTOR, "div.a-section #legalTextRow a[href*='condition_of_use']")