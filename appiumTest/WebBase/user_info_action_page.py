from appium.webdriver.common.mobileby import MobileBy

from appiumTest.WebBase.base_page import BasePage
from appiumTest.WebBase.edit_user_page import EditUserPage


class UserInfoActionPage(BasePage):
    def move_to_edit_user(self):
        self.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        return EditUserPage(self.driver)