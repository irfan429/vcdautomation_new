from webdriver.WebDriverHelper import WebDriverHelper
import logging

log = logging


class VCDMenuBar(WebDriverHelper):

    def __init__(self):
        WebDriverHelper.__init__(self)

    def click_updates_menu_icon(self):
        log.info("Find and click 'Updates' menu icon")
        update_xpath = "//div[contains(text(),'Updates')]"
        self.click_element(update_xpath, "Updates menu icon")

    def click_control_panel_menu_icon(self):
        log.info("Find and click 'Control Panel' menu icon")
        controlPanel_xpath = "//div[contains(text(),'Control Panel')]"
        self.click_element(controlPanel_xpath, "Control Panel menu icon")

    def click_building_menu_icon(self):
        log.info("Find and click 'Building' menu icon")
        update_xpath = "//div[contains(text(),'Building')]"
        self.click_element(update_xpath, "Building menu icon")

    def click_account_settings_menu_icon(self):
        log.info("Find and click 'Account settings' menu icon")
        update_xpath = "//div[contains(text(),'Account settings')]"
        self.click_element(update_xpath, "Account settings menu icon")
