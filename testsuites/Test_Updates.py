import os
import time
import allure
import pytest
from pytest_testrail.plugin import pytestrail

@pytest.mark.Regression
@pytestrail.case('C7246')
@allure.title("C7246: Verify that you can access VCD")
def test_case_C7246(test_case_template):
    new_case = test_case_template
    new_case.go_to_url(new_case.url)
    # new_case.click_updates_menu_icon()
    # new_case.click_upload_new_image_button()
    # new_case.pyauto_uploadFile("\\data\\newImageFile\\VIEW_NtWC_Pr10_MCU_2.4.5.tgz", 'enter')

    time.sleep(5)
