from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MessageListPage(BaseAction):

    # 新建短信
    new_message_button = By.ID, 'com.android.mms:id/action_compose_new'

    def click_new_message(self):
        self.click(self.new_message_button)