from appium.webdriver.common.mobileby import MobileBy

from appiumTest.WebBase.base_page import BasePage


class AddMemberPage(BasePage):
    def add_member_info_manually(self, username, mobileID, keep_add=True):
        self.find_element(MobileBy.XPATH, "//android.widget.LinearLayout//*[@text='手动输入添加']").click()
        self.find_element(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@text='必填']"). \
            send_keys(username)
        self.find_element(MobileBy.XPATH, "//*[contains(@text, '手机')]/..//*[@text='必填']"). \
            send_keys(mobileID)

        if keep_add:
            self.find_element(MobileBy.XPATH, "//android.widget.LinearLayout//*[@text='保存并继续添加']").click()
        else:
            self.find_element(MobileBy.XPATH, "//android.widget.LinearLayout//*[@text='保存']").click()

    def get_toast_notification(self):
        notification_text = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return notification_text

    def back_to_contact_list_page(self):
        self.driver.save_screenshot("./screenshot.png")
        self.find_element(MobileBy.ID, "com.tencent.wework:id/h86").click()









