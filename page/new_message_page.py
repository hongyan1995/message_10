from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class NewMessagePage(BaseAction):

    # 接收者
    recipients_edit_text = By.ID, 'com.android.mms:id/recipients_editor'

    # 输入的信息
    embedded_edit_text = By.ID, "com.android.mms:id/embedded_text_editor"

    # 发送按钮
    send_button = By.ID, "com.android.mms:id/send_button_sms"

    def input_recipients(self, content):
        self.input(self.recipients_edit_text, content)

    def input_embedded(self,  content):
        self.input(self.embedded_edit_text, content)

    def click_send(self):
        self.click(self.send_button)

    def is_has_content(self, message):
        xpath = "//*[@resource-id='com.android.mms:id/text_view' and @text='" + message + "']"
        try:
            self.find_element((By.XPATH, xpath))
            return True
        except TimeoutException:
            return False
        # except TimeoutException:
        # except ValueError:




