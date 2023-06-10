from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResult(Page):
    RESULT_TEXT = (By.XPATH, "//span[@class = 'a-color-state a-text-bold']")
    ALL_PRODUCTS = (By.XPATH,
                    "//div[@data-component-type='s-search-result']//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")

    def verify_search_result(self, expected_result):
        # actual_result = self.find_element(*self.RESULT_TEXT).text
        # assert expected_result == actual_result, f'Error !! Actual result {actual_result} is not equal to expected result/' \
        #                                          f'{expected_result}'
        self.verify_element_text(expected_result, *self.RESULT_TEXT)

    def product_page_displayed(self):
        self.all_prod = self.find_elements(*self.ALL_PRODUCTS)
        self.all_prod[0].click()

        sleep(5)

    def store_product(self):
        return self.find_element(*self.ALL_PRODUCTS).text
