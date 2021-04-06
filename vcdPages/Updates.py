import os
import allure
import logging
from webdriver.WebDriverHelper import WebDriverHelper

log = logging


class Updates(WebDriverHelper):

    def __init__(self):
        WebDriverHelper.__init__()

    def click_upload_new_file_button(self):
        log.info("Find and click 'Upload New File' button")
        uploadNewFile_button = "//div[text()='Upload New File']"
        self.click_element(uploadNewFile_button, "Upload New File button")

    def click_upload_new_image_button(self):
        log.info("Find and click 'Upload New Image' button")
        uploadNewImage_button = "//div[text()='Upload New Images']"
        self.click_element(uploadNewImage_button, "Upload New Image button")

    def select_software_version_to_upgrade(self, nodeName, version_no, comment ):
        log.info("Find and select 'given software version to upgrade' ")
        selection_xpath = "//div[text()='{}']/ancestor::div[contains(@class,'utils-update-software_rowContent')]//img[contains(@class,'dropdown_icon')]".format(nodeName)
        self.select_option_from_drop_down(selection_xpath, version_no, comment)

    def click_start_job_button(self):
        log.info("Find and click 'Start Job' button")
        start_button = "//div[contains(text(),'Start Job')]"
        self.click_element(start_button, "Start Job button")

    def upload_file(self, file_path):
        with allure.step('Find upload csv field'):
            log.info('Find upload csv field')
            upload_button = self.find_element('visible', 'xpath', "//input[@id='input-file']", '')

        with allure.step('Enter email into email address field'):
            log.info('Enter file into upload csv field')
            upload_button.clear()
            full_file_path = os.getcwd() + file_path
            log.info("File path for upload: {}".format(full_file_path))
            upload_button.send_keys(full_file_path)