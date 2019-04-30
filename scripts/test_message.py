from base.base_driver import init_driver
from page.page import Page


class TestMessage:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_send_message(self):
        self.page.message_list.click_new_message()
        self.page.new_message.input_recipients("18888888888")
        self.page.new_message.input_embedded("xxx")
        self.page.new_message.click_send()
        assert self.page.new_message.is_has_content("xxx")
