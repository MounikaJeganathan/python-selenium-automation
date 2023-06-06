import seconds as seconds
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

POPUP_SIGN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-signin-button")


@when('Verify signin is Clickable')
def sign_in_popup_clickable(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(POPUP_SIGN), message='Signin button is not clickable')


@then('wait for {time} seconds')
def wait_seconds(context, time):
    sleep(int(time))


@then('verify sign-in disappears')
def verify_signin_disappears(context):
    # context.driver.wait.until(
    #   EC.invisibility_of_element_located(POPUP_SIGN), message='Signin button is not disappeared')
    context.driver.wait.until_not(
        EC.visibility_of_element_located(POPUP_SIGN), message='Signin button is not disappeared')

    print('Test case passed')
