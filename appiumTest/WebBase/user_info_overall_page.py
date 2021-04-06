from appium.webdriver.common.mobileby import MobileBy

from appiumTest.WebBase.base_page import BasePage
from appiumTest.WebBase.user_info_action_page import UserInfoActionPage


class UserInfoOverallPage(BasePage):
    def move_to_user_action_page(self):
        self.find_element(MobileBy.ID, "com.tencent.wework:id/h8u").click()
        return UserInfoActionPage(self.driver)



