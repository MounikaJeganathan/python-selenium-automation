from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ORDERS_BTN = (By.XPATH, "//a[@id ='nav-orders']//span[@class ='nav-line-2']")
SIGN_IN_HEADER = (By.CSS_SELECTOR, "h1.a-spacing-small")
EMAIL_FIELD = (By.ID, 'ap_email')


@when('Click on orders')
def click_orders(context):
    context.app.header.click_orders()


@then('verify sign-in page is opened')
def verify_signin_opened(context):
    # assert context.driver.find_element(*SIGN_IN_HEADER).is_displayed(), \
    #     f'Error!!, Sign In header is not displayed '
    #
    # print("Sign in Page loaded sucessfully ")
    #
    # # verifies email field is present
    #
    # assert context.driver.find_element(*EMAIL_FIELD).is_displayed(), f'Error!! Email field is not displayed '
    #
    # print("Email field is displayed")

     context.app.signin_page.sigin_header()
     context.app.signin_page.email_field()
