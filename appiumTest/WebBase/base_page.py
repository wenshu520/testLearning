from appium.common.exceptions import NoSuchContextException
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver:WebDriver = None):
        self.driver = driver

    def find_element(self, by, value):
        element = self.driver.find_element(by, value)
        return element

    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)

    def swipe_find_element(self, locator, num=3):
        index = 0
        while index < num:
            num = num + 1
            try:
                self.driver.implicitly_wait(1)
                element = self.driver.find_element(MobileBy.XPATH, locator)
                self.driver.implicitly_wait(5)
                return element
            except Exception:
                width = self.driver.get_window_size()["width"]
                height = self.driver.get_window_size()["height"]
                x_start = width/2
                y_start = height * 0.8
                x_end = x_start
                y_end = height * 0.2
                self.driver.swipe(x_start, y_start, x_end, y_end, 1000)
        raise NoSuchContextException(f"No element {locator}")
