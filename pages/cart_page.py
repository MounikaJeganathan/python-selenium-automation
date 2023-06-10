import pages
from selenium.webdriver.common.by import By

from pages.base_page import Page
from pages.search_result import SearchResult


class Cart(Page):
    EMPTY_CART = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")
    Actual_prod = (By.CSS_SELECTOR, ".a-truncate-cut")
    SUB_TOTAL_CART = (By.ID, 'sc-subtotal-label-activecart')

    def verify_empty_cart(self):
        self.verify_is_displayed(*self.EMPTY_CART)
        print('Amazon Cart is empty')

    def verify_cart_name(self, expected_result):
        # assert self.product_name[:30] in self.verify_element_text(self.product_name, *self.Actual_prod), \
        #     f'Excepted {self.product_name} is not in cart'

        self.verify_partial_text(expected_result, *self.Actual_prod)
        print('Item added successfully')

    def verify_cart_quantity(self):
        self.quantity = self.find_element(*self.SUB_TOTAL_CART).text
        print(f'Number of items in cart is {self.quantity}')
        assert self.quantity != 0, f'Error!!, Item is not added in cart'
