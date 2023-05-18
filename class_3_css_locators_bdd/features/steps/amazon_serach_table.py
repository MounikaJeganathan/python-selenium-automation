from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_BTN = (By.ID, 'twotabsearchtextbox')
SEARCH_SUBMIT= (By.ID, 'nav-search-submit-button')

@given('Open Amazon main page')
def open_amazon(context):
    context.driver.get("https://www.amazon.com/")


@when('Search for {search_item}')
def search_product(context, search_item):
    context.driver.find_element(*SEARCH_BTN).send_keys(search_item)
    context.driver.find_element(*SEARCH_SUBMIT).click()


@then('verify search result shown for {expected_result}')
def verify_product(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class = 'a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Error !! Actual result {actual_result} is not equal to expected result/' \
                                             f'{expected_result}'

    print("Test case is passed")
