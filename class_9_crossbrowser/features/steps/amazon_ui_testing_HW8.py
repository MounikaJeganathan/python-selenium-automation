from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/gp/product/{product_id}/')

@when('Select department baby')
def select_department(context):
    context.app.header.select_depart_baby()

@when('Hover on New Arrivals')
def hover_new_arrivals(context):
    context.app.header.hover_new_arrivals()


@then('Verify correct department shown as baby')
def verify_department_shown(context):
    context.app.search_result.verify_sub_dept_baby()
    print("Test case passed")


@then('Verify deals are displaying')
def verify_deals_display(context):
    context.app.search_result.verify_deals_display()
    print("Test case passed")

