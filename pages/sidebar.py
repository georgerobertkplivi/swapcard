from pages.base_page import BasePage


class SideBar(BasePage):
    hamburger_menu_selector = ".hm-icon"
    arts_and_craft_selector = "//div[.='Arts & Crafts']"
    beading_selector = "//a[.='Beading & Jewelry Making']"

    def click_menu(self):
        self.click_web_element(self.hamburger_menu_selector)

    def click_arts_link(self):
        self.click_web_element(self.arts_and_craft_selector)

    def click_beading_link(self):
        self.click_web_element(self.beading_selector)

