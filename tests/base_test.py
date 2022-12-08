from seleniumbase import BaseCase


class BaseTest(BaseCase):
    base_url = "https://www.amazon.com"

    def setUp(self):
        super(BaseTest, self).setUp()
        self.open(self.base_url)

    def tearDown(self):
        self.save_teardown_screenshot()  # If test fails, or if "--screenshot" is used in cli
        super(BaseTest, self).tearDown()
