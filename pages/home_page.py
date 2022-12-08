from pages.sidebar import SideBar


class HomePage(SideBar):
    def wait_for_page_to_load(self):
        self.is_element_present("#nav-logo-sprites")
        self.is_element_present("[data-csa-c-slot-id='nav_cs_0']")
        self.is_element_present("[data-csa-c-slot-id='nav_cs_1']")
        self.is_element_present("[data-csa-c-slot-id='nav_cs_2']")
        self.is_element_present("[data-csa-c-slot-id='nav_cs_3']")
        self.is_element_present("[data-csa-c-slot-id='nav_cs_4']")
        self.is_element_present("#swm-link")

    def select_beadind_and_jewelry_making(self):
        self.wait_for_page_to_load()
        self.click_menu()
        self.click_arts_link()
        self.click_beading_link()