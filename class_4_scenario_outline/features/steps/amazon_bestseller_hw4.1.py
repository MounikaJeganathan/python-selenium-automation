from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BESTSELLER_ICON = (By.XPATH, "//a[contains(text(),'Best Sellers')]")
BESTSELLER_LINKS = (By.CSS_SELECTOR, "#zg_header a")


@when('Click on Best Seller')
def click_bestseller(context):
    context.driver.find_element(*BESTSELLER_ICON).click()


@then('Verify the {expected_links} links')
def verify_links(context, expected_links):
    expected_links = int(expected_links)
    all_links = len(context.driver.find_elements(*BESTSELLER_LINKS))
    assert all_links == expected_links, f'Error!!!Expected {expected_links} but acutal is {all_links}'
    print("Links are 5 as expected , test case passed !!")
