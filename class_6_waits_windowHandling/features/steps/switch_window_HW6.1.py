from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

PRIVACY_NOTICE = (By.XPATH, "//a[contains(@href,'https://www.amazon.com/privacy')]")


@given('Open Amazon T&C page')
def Open_Amazon_T_page(context):
    context.driver.get \
        ('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_'
         'of_use?ie=UTF8&nodeId=508088')


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice(context):
    context.driver.find_element(*PRIVACY_NOTICE).click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    all_windows_in_page = context.driver.window_handles
    print("After new window opened , all windows are  :", all_windows_in_page)
    context.driver.switch_to.window(all_windows_in_page[1])


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_page_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer'))


@then('User can close new window and switch back to original')
def close_window_switch(context):
    context.driver.close()
    all_windows_in_page = context.driver.window_handles
    print("After new window opened , all windows are  :", all_windows_in_page)
    context.driver.switch_to.window(context.original_window)

    print("Test case passed")
