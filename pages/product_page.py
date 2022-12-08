import re

from pages.results_page import ResultsPage


class ProductPage(ResultsPage):
    add_to_cart_button_selector = "add-to-cart-button"
    buy_button_selector = "buy-now-button"
    customer_review_selector = "#reviewsMedley h2"
    stars = "//div[@id='averageCustomerReviews']"
    star_rating_text_selector = "[data-hook='rating-out-of-text']"
    price_selector = "//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']" \
                     "//span[@class='a-price-whole']"

    def wait_for_product_page_to_load(self):
        self.is_element_present(self.add_to_cart_button_selector)
        self.is_element_present(self.buy_button_selector)
        self.is_element_present(self.buy_button_selector)

    def get_product_price(self):
        price = self.get_text(self.price_selector)
        return float(price.replace(",", ""))

    def get_star_rating(self):
        self.scroll_to(self.customer_review_selector)
        if self.is_element_present(self.star_rating_text_selector):
            rating = self.get_text(self.star_rating_text_selector)
            rating_number = re.findall(r"[-+]?\d*\.\d+|\d+", rating)
            return float(rating_number[0])

