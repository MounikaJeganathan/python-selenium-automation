from time import sleep

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
driver.get(
    'https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&mobileBrowserWeblabTreatment=C&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fdp%2FB0BN91GD3J%3Ftag%3Damz-mkt-chr-us-20%26ascsubtag%3D1ba00-01000-a0049-win10-other-smile-us000-pcomp-feature-scomp-feature-scomp%26ref%3Dnav_ya_signin%26th%3D1&prevRID=YNC72Q38RKQWV5PD71E4&openid.assoc_handle=usflex&openid.mode=checkid_setup&desktopBrowserWeblabTreatment=C&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

sleep(10)

# By using Css with class- amazon
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')
driver.find_element(By.CSS_SELECTOR, "i.a-icon[aria-label = 'Amazon']")

# By using CSS - create Account
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')
driver.find_element(By.CSS_SELECTOR, 'div.a-box-inner h1.a-spacing-small')

# CSS - your name
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name[name='customerName']")
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name[name='customerName']")
driver.find_element(By.CSS_SELECTOR, "[name='customerName'][autocomplete='name']")

# CSS - Email
driver.find_element(By.CSS_SELECTOR, 'input#ap_email')
driver.find_element(By.CSS_SELECTOR, 'input#ap_email.a-input-text')
driver.find_element(By.CSS_SELECTOR, "#ap_email[data-validation-id='email']")

# Css - Password
driver.find_element(By.CSS_SELECTOR, "#ap_password")
driver.find_element(By.CSS_SELECTOR, "#ap_password.a-input-text.a-span12")
driver.find_element(By.CSS_SELECTOR, "#ap_password.a-input-text.a-span12[placeholder='At least 6 characters']")
driver.find_element(By.CSS_SELECTOR, "[placeholder='At least 6 characters'][name='password']")

# CSS - reenter password
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
driver.find_element(By.CSS_SELECTOR, "#ap_password_check[name='passwordCheck']")

# CSS - Continue button
driver.find_element(By.CSS_SELECTOR, '#continue')
driver.find_element(By.CSS_SELECTOR, '#continue.a-button-input')
driver.find_element(By.CSS_SELECTOR, "#continue[type='submit']")

# CSS - Condition to use link
driver.find_element(By.CSS_SELECTOR, "a[href*='condition_of_use?']")
driver.find_element(By.CSS_SELECTOR, "div#legalTextRow a[href*='condition_of_use?']")

# CSS - Privacy notice link
driver.find_element(By.CSS_SELECTOR, "a[href*='privacy_notice']")
driver.find_element(By.CSS_SELECTOR, "div#legalTextRow a[href*='privacy_notice']")

# CSS - Sign in
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis[href*='signin?openid']")
driver.find_element(By.CSS_SELECTOR, "div.a-row a[href*='signin?openid']")
