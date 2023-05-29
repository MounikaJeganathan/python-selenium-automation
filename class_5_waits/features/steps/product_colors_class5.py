from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@then('Verify user can click through colors')
def verify_can_click_colors(context):
    expected_colors = ['Army Green', 'Black', 'Brown', 'Burgundy']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors[:4]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors += [current_color]

    assert expected_colors == actual_colors, \
        f'Expected colors {expected_colors} did not match actual {actual_colors}'
    print('Test case passed')
