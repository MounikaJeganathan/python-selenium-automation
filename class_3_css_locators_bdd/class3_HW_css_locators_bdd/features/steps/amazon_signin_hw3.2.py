from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Amazon main page')
def open_amazon(context):
    context.driver.get("https://www.amazon.com/")


@when('Click on orders')
def click_orders(context):
    context.driver.find_element(By.XPATH, "//a[@id ='nav-orders']//span[@class ='nav-line-2']").click()


@then('verify sign-in page is opened')
def verify_signin_opened(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small").is_displayed(), \
        f'Error!!, Sign In header is not displayed '

    print("Sign in Page loaded sucessfully ")

    # verifies email field is present

    assert context.driver.find_element(By.ID, 'ap_email').is_displayed(), f'Error!! Email field is not displayed '

    print("Email field is displayed")
