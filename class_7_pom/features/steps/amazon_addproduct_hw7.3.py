from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_BTN = (By.ID, 'twotabsearchtextbox')
SEARCH_SUBMIT = (By.ID, 'nav-search-submit-button')
ADD_TO_CART = (By.ID, 'add-to-cart-button')
CART_BTN = (By.ID, 'nav-cart-count')
SUB_TOTAL_CART = (By.ID, 'sc-subtotal-label-activecart')
ALL_PRODUCTS = (By.XPATH,
                "//div[@data-component-type='s-search-result']//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")

Actual_prod = (By.CSS_SELECTOR, ".a-truncate-cut")


@when('search the item coffee')
def search_item(context):
    # context.driver.find_element(*SEARCH_BTN).send_keys('coffee')
    # context.driver.find_element(*SEARCH_SUBMIT).click()
    context.app.header.search_product('coffee')


@then('Add the coffee link to cart')
def add_item_to_cart(context):
    # all_prod = context.driver.find_elements(*ALL_PRODUCTS)
    # all_prod[0].click()
    # sleep(5)
    # context.driver.find_element(*ADD_TO_CART).click()
    context.app.search_result.product_page_displayed()
    context.app.product_page.click_add_on_cart()


@then('Store the product name')
def store_product(context):
    # context.product_name = context.driver.find_element(*ALL_PRODUCTS).text
    # print(f'Current product name is {context.product_name}')
    context.product_name = context.app.search_result.store_product()
    print(f'Current product name is {context.product_name}')


@then('Click on amazon cart')
def click_cart(context):
    # context.driver.find_element(*CART_BTN).click()
    context.app.header.click_cart()


@then('Verify the coffee is added successfully in cart')
def verifying_cart(context):
    # acutal_name = context.driver.find_element(*Actual_prod).text
    # quantity = context.driver.find_element(*SUB_TOTAL_CART).text
    # print(f'Number of items in cart is {quantity}')
    # assert quantity != 0, f'Error!!, Item is not added in cart'
    # assert context.product_name[:30] in acutal_name, f'Excepected {context.product_name} is not in cart'
    # print('Item added successfully')
    context.current_product = context.product_name[:30]
    context.app.cart_page.verify_cart_name(context.current_product)
    context.app.cart_page.verify_cart_quantity()
