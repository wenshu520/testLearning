import yaml
from appium import webdriver

from appiumTest.WebBase.base_page import BasePage
from appiumTest.WebBase.main_page import MainPage


class App(BasePage):
    def start_app(self):
        if not self.driver:
            with open('../config/conf.yaml') as configfile:
                confs = yaml.load(configfile)
            print(confs)
            caps = confs["desiredCap"]
            ip = confs["appiumServer"]["ip"]
            port = confs["appiumServer"]["port"]
            # 客户端与appium server 建立连接
            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def restart_app(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop_app(self):
        self.driver.quit()

    def goto_main(self):
        return MainPage(self.driver)



