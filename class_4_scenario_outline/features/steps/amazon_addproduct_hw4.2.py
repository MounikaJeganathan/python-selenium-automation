from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_BTN = (By.ID, 'twotabsearchtextbox')
SEARCH_SUBMIT = (By.ID, 'nav-search-submit-button')
ADD_TO_CART = (By.ID, 'add-to-cart-button')
CART_BTN = (By.ID, 'nav-cart-count')
SUB_TOTAL_CART = (By.ID, 'sc-subtotal-label-activecart')

@when('search the item coffee')
def search_item(context):
    context.driver.find_element(*SEARCH_BTN).send_keys('coffee')
    context.driver.find_element(*SEARCH_SUBMIT).click()


@then('Add the coffee link to cart')
def add_item_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,
                                "div.a-section img.s-image[alt='Sponsored Ad - AmazonFresh Organic Fair Trade Sumatra Ground Coffee, Dark Roast, 12 Ounce']").click()
    sleep(5)
    context.driver.find_element(*ADD_TO_CART).click()


@then('Click on amazon cart')
def click_cart(context):
    context.driver.find_element(*CART_BTN).click()


@then('Verify the coffee is added successfully in cart')
def verifying_cart(context):
    assert context.driver.find_element(By.XPATH,
                                       "//span[@class='a-truncate-cut' and contains(text(),'AmazonFresh Organic Fair Trade Sumatra Ground Coffee,')]").is_displayed(),\
        f'Error!!, Item is not added in cart'
    print('Item added successfully')
    quantity = context.driver.find_element(*SUB_TOTAL_CART).text
    print(f'Number of items in cart is {quantity}')

