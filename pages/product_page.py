from selenium.webdriver.common.by import By

from pages.base_page import Page


class ProductPage(Page):
    ADD_TO_CART = (By.ID, 'add-to-cart-button')

    def click_add_on_cart(self):
        self.click(*self.ADD_TO_CART)
