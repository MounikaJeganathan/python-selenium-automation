from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open amazon link')
def open_amazon_link(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div#nav-cart-count-container span.nav-cart-icon').click()


@then('Verify amazon cart is empty')
def cart_empty(context):
    assert context.driver.find_element(By.XPATH,"//div[@class='a-row sc-your-amazon-cart-is-empty']").is_displayed(),\
            f'Error!!, Cart is not empty'
    print('Amazon Cart is empty')
