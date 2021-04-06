from appium.webdriver.common.mobileby import MobileBy

from appiumTest.WebBase.add_member_page import AddMemberPage
from appiumTest.WebBase.base_page import BasePage
from appiumTest.WebBase.user_info_overall_page import UserInfoOverallPage


class ContactListPage(BasePage):
    def move_to_add_memeber_page(self):
        self.swipe_find_element("//android.view.ViewGroup//*[@text='添加成员']").click()
        return AddMemberPage(self.driver)

    def search_user(self, username):
        self.find_element(MobileBy.ID, "com.tencent.wework:id/h8q").click()
        self.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys(username)
        elements = self.find_elements(MobileBy.XPATH, f"//android.widget.ListView//*[@text='{username}']")
        if len(elements) > 0:
            return elements[0]
        else:
            return False
            print(f"User: {username} doesn't exist")

    def move_to_user_info_page(self, username):
        self.swipe_find_element(f"//*[@text='{username}']").click()
        return UserInfoOverallPage(self.driver)
