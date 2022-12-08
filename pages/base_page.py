from seleniumbase import BaseCase


class BasePage(BaseCase):

    def click_web_element(self, selector):
        self.click(selector)

    def send_text(self, selector):
        self.type(selector)