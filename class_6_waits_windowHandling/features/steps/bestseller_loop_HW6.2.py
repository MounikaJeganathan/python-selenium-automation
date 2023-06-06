from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

BEST_SELLER = (By.XPATH, "//a[contains(text(),'Best Sellers')]")
LINKS_BESTSELLER = (By.CSS_SELECTOR, '#zg_header a')
HEADER = (By.CSS_SELECTOR, "#zg_banner_text")


@given('Click on Best Seller')
def click_best_seller(context):
    context.driver.find_element(*BEST_SELLER).click()


@then('Verify all the sub links page is working')
def verify_all_links_open(context):
    top_links = context.driver.find_elements(*LINKS_BESTSELLER)
    for i in range(len(top_links)):
        link_click = context.driver.find_elements(*LINKS_BESTSELLER)[i]
        text_in_link = link_click.text
        link_click.click()

        text_in_header = context.driver.find_element(*HEADER).text
        assert text_in_link in text_in_header, f'Error!! Excepted {text_in_link} not in {text_in_header}'

    print("Test case Passed")