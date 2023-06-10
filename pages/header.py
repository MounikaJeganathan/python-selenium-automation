from selenium.webdriver.common.by import By

from pages.base_page import Page


class Header(Page):
    SEARCH_BTN = (By.ID, 'twotabsearchtextbox')
    SEARCH_SUBMIT = (By.ID, 'nav-search-submit-button')
    ORDERS_BTN = (By.XPATH, "//a[@id ='nav-orders']//span[@class ='nav-line-2']")
    CART_ICON = (By.CSS_SELECTOR, 'div#nav-cart-count-container span.nav-cart-icon')
    CART_BTN = (By.ID, 'nav-cart-count')

    def search_product(self, search_item):
        self.input_text(search_item, *self.SEARCH_BTN)
        self.click(*self.SEARCH_SUBMIT)

    def click_orders(self):
        self.click(*self.ORDERS_BTN)

    def click_cart(self):
        self.click(*self.CART_BTN)
