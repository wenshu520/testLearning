from appium.webdriver.common.mobileby import MobileBy

from appiumTest.WebBase.base_page import BasePage


class EditUserPage(BasePage):
    def remove_user(self):
        self.swipe_find_element("//*[@text='删除成员']").click()
        self.find_element(MobileBy.XPATH, "//*[@text='确定']").click()