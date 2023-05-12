from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open amazon page')
def open_link(context):
    context.driver.get("https://www.amazon.com/")
    sleep(5)


@when('search the item coffee')
def search_item(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee')
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then('Add the coffee link to cart')
def add_item_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,
                                "div.a-section img.s-image[alt='Sponsored Ad - AmazonFresh Go For The Bold Ground Coffee, Dark Roast, 12 Ounce']").click()
    sleep(5)
    context.driver.find_element(By.ID, 'add-to-cart-button').click()


@then('Click on amazon cart')
def click_cart(context):
    context.driver.find_element(By.ID, 'nav-cart-count').click()


@then('Verify the coffee is added successfully in cart')
def verifying_cart(context):
    assert context.driver.find_element(By.XPATH,
                                       "//span[@class = 'a-truncate-cut' and contains(text(), 'AmazonFresh Go For The Bold')]").is_displayed(),\
        f'Error!!, Item is not added in cart'
    print('Item added successfully')
    quantity = context.driver.find_element(By.ID, 'sc-subtotal-label-activecart').text
    print(f'Number of items in cart is {quantity}')

