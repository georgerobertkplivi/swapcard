from pages.product_page import ProductPage
from pages.sort_category.sort import SortBy
from tests.base_test import BaseTest


class AmazonTest(BaseTest, ProductPage):

    ## Check the review score. If it's less than 4, fail the test, otherwise pass it
    def test_product_rating_less_than_4(self):
        self.select_beadind_and_jewelry_making()
        self.click_engraving_link()
        self.click_sort_by_dropdown()
        self.select_sort_by_type(SortBy.HIGH_TO_LOW.value)
        self.open_product(3)
        self.wait_for_product_page_to_load()
        self.get_star_rating()
        self.assertTrue(self.get_star_rating() < 4)

    ##  Check the price for the opened item. If it's more than $4000, fail the test, otherwise pass it.
    def test_product_price_less_than_4000(self):
        self.select_beadind_and_jewelry_making()
        self.click_engraving_link()
        self.click_sort_by_dropdown()
        self.select_sort_by_type(SortBy.HIGH_TO_LOW.value)
        self.open_product(3)
        self.wait_for_product_page_to_load()
        self.assertTrue(self.get_product_price() <= 4000, "Product Price is above $4000")
