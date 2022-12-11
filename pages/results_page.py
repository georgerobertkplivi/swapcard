import time

from pages.home_page import HomePage


class ResultsPage(HomePage):
    engraving_machine_selector = "//span[.='Engraving Machines & Tools']"
    sort_by_selector = ".a-dropdown-prompt"

    def wait_for_results_page_to_load(self):
        results_selector = ".a-text-normal.a-size-medium-plus"
        self.is_element_present(results_selector)
        self.assert_text("RESULTS", results_selector)

    def select_sort_by_type(self, sort_category):
        self.click("//a[.='" + sort_category + "']")

    def get_sort_by_type_text(self):
        self.get_text("//span[@class='a-button-text a-declarative']")

    def click_sort_by_dropdown(self):
        self.click_web_element(self.sort_by_selector)

    def click_engraving_link(self):
        self.click_web_element(self.engraving_machine_selector)

    def open_product(self, item_position):
        product_selector = "[cel_widget_id='MAIN-SEARCH_RESULTS-" + str(item_position) + "'] .a-size-mini > .a-link-normal"
        self.scroll_to(product_selector)
        self.click_web_element(product_selector)
        self.assertTrue(self.is_element_present(".ssf-share-trigger"))
