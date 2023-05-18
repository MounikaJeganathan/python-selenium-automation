from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

FOOTER_LINKS = (By.CSS_SELECTOR, ".navFooterMoreOnAmazon .navFooterDescItem")


@then('Verify there are {expected_no_of_links}footer links')
def verify_footer_link(context, expected_no_of_links):
    expected_no_of_links= int(expected_no_of_links)
    links_counts = len(context.driver.find_elements(*FOOTER_LINKS))
    #print(context.driver.find_elements(*FOOTER_LINKS))
    #print(type(context.driver.find_elements(*FOOTER_LINKS)))
    #assert links_counts > 6, f'Error!!! Expected more than 1 link'
    assert links_counts == expected_no_of_links, f'Error!!! Expected {expected_no_of_links} but acutal is {links_counts}'
    print('Links are 36 as expected,  test case passed !!')
