from appium.webdriver.common.mobileby import MobileBy

from appiumTest.WebBase.base_page import BasePage
from appiumTest.WebBase.contact_list_page import ContactListPage


class MainPage(BasePage):
    def go_to_contact_list_page(self):
        self.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return ContactListPage(self.driver)