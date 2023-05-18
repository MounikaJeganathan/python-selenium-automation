from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

WELCOME_NOTE = (By.XPATH, "//h1[contains(text(),'Welcome to Amazon Customer Service')]")
UI_Element = (By.CSS_SELECTOR, "div.issue-card-container .issue-card-wrapper")
LIB_SECTION = (By.XPATH, "//h2[contains(text(),'Search our help library')]")
LIB_TAB = (By.ID, "hubHelpSearchInput")
HELP_TOPICS = (By.CSS_SELECTOR, "ul.help-topics .help-topics")


@given('Open Customerservice page')
def open_cust_service(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Verify welcome note present')
def verify_welcome_note(context):
    assert context.driver.find_element(*WELCOME_NOTE).is_displayed(), f'Error!!, Welcome note is not displayed'
    print("Welcome note is displayed")


@then('Verify {no_of_UI}UI element')
def verify_ui(context, no_of_UI):
    no_of_UI = int(no_of_UI)
    ui_links = len(context.driver.find_elements(*UI_Element))
    assert ui_links == no_of_UI, f'ERROR!!!, Expected {no_of_UI} but got {ui_links}'
    print("UI link are 10 as expected , test case passed !!")


@then('Verify library tab')
def verify_lib_tab(context):
    assert context.driver.find_element(*LIB_SECTION).is_displayed(), f'Error!!, Library section is not displayed'
    print("Library section is displayed")
    assert context.driver.find_element(*LIB_TAB).is_displayed(), f'Error!!, Library textbox is not displayed'
    print("Library Textbox is displayed")


@then('Verify {help_links} help topics')
def verify_help_topics(context, help_links):
    help_links = int(help_links)
    total_help_links = len(context.driver.find_elements(*HELP_TOPICS))
    assert total_help_links == help_links, f'Error!!!Expected {help_links} but acutal is {total_help_links}'
    print("Helplinks totally 11 as expected , test case passed !!")
