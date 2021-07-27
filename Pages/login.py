from webdriver.WebDriverHelper import WebDriverHelper
import logging

log = logging


class Login(WebDriverHelper):

    def __int__(self):
        WebDriverHelper.__init__(self)

    def login_fusion(self, username, password):
        user_name_xpath = "//input[@id='Login1_UserName']"
        password_id = "//input[@id='Login1_Password']"
        login_button_xpath = "//input[@id='Login1_Login']"

        self.uname = self.find_element('visible', 'css', user_name_xpath, 20)
        self.uname.send_keys(username)

        self.password = self.find_element('visible', 'xpath', password_id, 10)
        self.password.send_keys(password)

        self.login_button = self.find_element('visible', 'xpath', login_button_xpath, 10)
        self.login_button.click()

    def logout_fusion(self):
        logout_button_xpath = "#logout"

        self.button = self.find_element('visible', 'css', logout_button_xpath, 20)
        self.button.click()