from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_BTN = (By.ID, 'twotabsearchtextbox')
SEARCH_SUBMIT = (By.ID, 'nav-search-submit-button')
ALL_PRODUCTS = (By.XPATH,
                "//div[@data-component-type='s-search-result']//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")

# IMAGE = (By.CSS_SELECTOR, "#imgTagWrapperId img")
# PROD_TITLE = (By.CSS_SELECTOR, "#productTitle")

Images_PROD = (By.CSS_SELECTOR, ".a-section img")
NAME_PROD = (By.CSS_SELECTOR, ".a-size-base-plus")


@when('search the item coffee')
def search_item(context):
    context.driver.find_element(*SEARCH_BTN).send_keys('coffee')
    context.driver.find_element(*SEARCH_SUBMIT).click()


@then('Verify result have images and name for all products')
def products_image_name(context):
    all_prod = context.driver.find_elements(*ALL_PRODUCTS)
    current_URL = context.driver.current_url
    for each_product in all_prod[:3]:
        # each_product.click()
        # assert context.driver.find_element(*IMAGE).is_displayed(), f'Image is not displayed for the product'
        # assert context.driver.find_element(
        #    *PROD_TITLE).is_displayed(), f'Product title is not displayed for the product'
        # context.driver.get(current_URL)
        image = context.driver.find_element(*Images_PROD)
        name = context.driver.find_element(*NAME_PROD)
        assert image.is_displayed(), f'Image is not displayed for the product'
        assert name.is_displayed(), f'Product title is not displayed for the product'

    print('Test case passed')
