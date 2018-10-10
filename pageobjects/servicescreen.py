import pytest
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from drivers.webdriver import Driver
from selenium import webdriver



from pageobjects.homescreen import HomeScreen
from pageobjects.basepage import BasePage


class ServiceScreen(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.page_title = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.ID, "page-title")))
        self.page_title_label = self.driver.instance.find_element_by_id("page-title").text
        self.photo_book_design_image = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="block-system-main"]/div/div/div/div/div[1]/div/div/a/img')))
        self.photo_book_design_link = WebDriverWait(self.driver.instance,10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'views-field views-field-title')))
        #self.photo_book_design_label = self.driver.instance.find_element_by_id("page-title").text
        #print(self.page_title_label)


    #@pytest.allure.step("Validate page title is visible")
    def validate_page_title_is_visible(self):
        assert self.page_title.is_displayed()
        assert self.page_title_label == 'SERVICES'
        #assert self.page_title.

    def validate_photo_book_design_image(self):
        assert self.photo_book_design_image.is_displayed()
        assert self.photo_book_design_image.is_displayed()
        assert self.photo_book_design_link.text == 'PHOTOBOOK DESIGN'

    #def validate_referral_service_image(self):
    #    assert self.referral_service_image.is_displayed()




