from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@given('Open Amazon main page')
def open_amazon(context):
    context.app.main_page.open_main_page()


@when('Hover over the language option')
def hover_lang(context):
    context.app.header.hover_lang()


@when('Select department books')
def select_department(context):
    context.app.header.select_depart_book()


@when('Search for {search_item}')
def search_product(context, search_item):
    context.app.header.search_product(search_item)


@then('Verify Spanish option present')
def verify_spanish_lang(context):
    context.app.header.verify_spanish_lang()
    print("Test case passed")

@then('Verify correct department shown as book')
def verify_department_shown(context):
    context.app.search_result.verify_sub_dept_book()
    print("Test case passed")
