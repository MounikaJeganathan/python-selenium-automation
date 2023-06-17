from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import Page


class Header(Page):
    SEARCH_BTN = (By.ID, 'twotabsearchtextbox')
    SEARCH_SUBMIT = (By.ID, 'nav-search-submit-button')
    ORDERS_BTN = (By.XPATH, "//a[@id ='nav-orders']//span[@class ='nav-line-2']")
    CART_ICON = (By.CSS_SELECTOR, 'div#nav-cart-count-container span.nav-cart-icon')
    CART_BTN = (By.ID, 'nav-cart-count')
    LANG_OPTION = (By.ID, 'icp-nav-flyout')
    SPANISH_LANG = (By.CSS_SELECTOR, "a[href='#switch-lang=es_US']")
    DEPART_SELECT = (By.ID, "searchDropdownBox")
    NEW_ARRIVALS = (By.XPATH, "//span[contains(text(),'New Arrivals')]")

    def search_product(self, search_item):
        self.input_text(search_item, *self.SEARCH_BTN)
        self.click(*self.SEARCH_SUBMIT)

    def click_orders(self):
        self.click(*self.ORDERS_BTN)

    def click_cart(self):
        self.click(*self.CART_BTN)

    def hover_lang(self):
        lang_options = self.driver.find_element(*self.LANG_OPTION)
        actions = ActionChains(self.driver)
        actions.move_to_element(lang_options)
        actions.perform()
        sleep(3)

    def verify_spanish_lang(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def select_depart_book(self):
        dept_select = self.find_element(*self.DEPART_SELECT)
        select = Select(dept_select)
        select.select_by_value("search-alias=stripbooks")

    def select_depart_baby(self):
        dept_select = self.find_element(*self.DEPART_SELECT)
        select = Select(dept_select)
        select.select_by_value("search-alias=baby-products")

    def hover_new_arrivals(self):
        new_arrivals = self.driver.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()
        sleep(3)
