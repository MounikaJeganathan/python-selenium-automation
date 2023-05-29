from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

POPUP_SIGN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-signin-button")
EMAIL= (By.ID, 'ap_email')
HEADER_SIGN_IN = (By.CSS_SELECTOR, "h1.a-spacing-small")


@given('Open Amazon main page')
def open_amazon(context):
    context.driver.get("https://www.amazon.com/")


@when('Click button from signin popup')
def sign_in_popup(context):
    sign_in_popup = context.driver.wait.until(
        EC.element_to_be_clickable(POPUP_SIGN), message='Signin button is not clickable')
    sign_in_popup.click()

@then('verify sign-in page is opened')
def verify_signin_opened(context):
    #Verifying the email :
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))
    assert context.driver.find_element(*HEADER_SIGN_IN).is_displayed(), \
        f'Error!!, Sign In header is not displayed '

    print("Sign in Page loaded sucessfully ")

    # verifies email field is present

    assert context.driver.find_element(*EMAIL).is_displayed(), f'Error!! Email field is not displayed '

