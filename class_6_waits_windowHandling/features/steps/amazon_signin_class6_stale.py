from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ORDERS_BTN = (By.XPATH, "//a[@id ='nav-orders']//span[@class ='nav-line-2']")
SIGN_IN_HEADER = (By.CSS_SELECTOR, "h1.a-spacing-small")
EMAIL_FIELD= (By.ID, 'ap_email')
@given('Open Amazon main page')
def open_amazon(context):
    context.driver.get("https://www.amazon.com/")


@when('Click on orders')
def click_orders(context):
    element= context.driver.find_element(*ORDERS_BTN)
    print('Before refresh: ', element)
    context.driver.refresh()
    #element = context.driver.find_element(*ORDERS_BTN)
    #WE will get stale element exception if we dont find the element again after refreshing it

    print('After refresh: ', element)
    element.click()



@then('verify sign-in page is opened')
def verify_signin_opened(context):
    assert context.driver.find_element(*SIGN_IN_HEADER).is_displayed(), \
        f'Error!!, Sign In header is not displayed '

    print("Sign in Page loaded sucessfully ")

    # verifies email field is present

    assert context.driver.find_element(*EMAIL_FIELD).is_displayed(), f'Error!! Email field is not displayed '

    print("Email field is displayed")
