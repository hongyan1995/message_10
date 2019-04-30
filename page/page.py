from page.message_list_page import MessageListPage
from page.new_message_page import NewMessagePage


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def message_list(self):
        return MessageListPage(self.driver)

    @property
    def new_message(self):
        return NewMessagePage(self.driver)