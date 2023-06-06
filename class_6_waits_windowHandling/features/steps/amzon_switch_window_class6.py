from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

DOG_IMAGE = (By.CSS_SELECTOR, "img[alt='Dogs of Amazon']")


@given('Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@given('Store Original window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print(f'Orginal window name is {context.original_window}')
    print(f'All window is {context.driver.window_handles}')


@when('Click on dog image')
def click_dog_name(context):
    context.driver.find_element(*DOG_IMAGE).click()


@when('Switch to new window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    all_windows = context.driver.window_handles
    print("After new window opened , all windows are  :", all_windows)
    context.driver.switch_to.window(all_windows[1])


@then('Verify blog is opened')
def verify_blog_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.aboutamazon.com/news/workplace'))


@then('close blog')
def close_blog(context):
    context.driver.close()
    all_windows = context.driver.window_handles
    print("After blog closed , all windows are  :", all_windows)

@then('Return to orginial window')
def return_original_window(context):
    context.driver.switch_to.window(context.original_window)

    print("Test case passed")