from webdriver.WebDriverHelper import WebDriverHelper
import logging

log = logging


class ControlPanel(WebDriverHelper):

    def __int__(self):
        WebDriverHelper.__init__()

    def click_connectivity_button(self):
        log.info("Find and click 'Connectivity' button")
        connectivity_button = "//div[contains(text(),'Connectivity')]"
        self.click_element(connectivity_button, "Connectivity button")

    def click_igus_button(self):
        log.info("Find and click 'IGUS' button")
        igus_button = "//div[contains(text(),'IGUS')]"
        self.click_element(igus_button, "IGUS button")

    def click_rediscover_network_button(self):
        log.info("Find and click 'Rediscover Network' button")
        rediscover_network_button = "//div[contains(text(),'Rediscover Network')]"
        self.click_element(rediscover_network_button, "Rediscover Network button")
