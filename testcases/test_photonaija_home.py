import unittest
import pytest
import allure
import os
import sys
sys.path.insert(0, '/users/jimiadekoya/pythonAutomationFramework')
from selenium import webdriver
from drivers.webdriver import Driver
#from drivers import webdriver
#from selenium import Driver
from values import strings
from pageobjects import homescreen,servicescreen











class TestPhotoNaija(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)
        self.home_screen = homescreen.HomeScreen(self.driver)
        self.home_screen.click_service_screen_link()
        self.service_screen = servicescreen.ServiceScreen(self.driver)
        #self.driver.instance.find_element_by_id()



    @pytest.allure.step("Validate Site title is visible")
    def test_home_screen_site_title(self):
        self.home_screen.validate_title_is_present()

    @pytest.allure.step("Validate Site icon is visible")
    def test_home_screen_site_icon(self):
        self.home_screen.validate_icon_is_present()

    @pytest.allure.step("Validate top menu is visible")
    def test_home_screen_top_menu(self):
        self.home_screen.validate_top_menu_is_present()

    @pytest.allure.step("Validate instagram button is visible")
    def test_home_screen_instagram(self):
        self.home_screen.validate_instagram_button_is_displayed()

    @pytest.allure.step("common pag components")
    def test_services_screen_common_components(self):
        #home_screen = homescreen.HomeScreen(self.driver)
    #Service page tests
    #@pytest.allure.step("Validate Site title is visible on the service page")
    #def test_service_screen_site_title(self):
        self.service_screen.validate_title_is_present()

    #@pytest.allure.step("Validate Site icon is visible on the service page")
    #def test_service_screen_site_icon(self):
        self.service_screen.validate_icon_is_present()

    #@pytest.allure.step("Validate top menu is visible on the service page")
    #def test_service_screen_top_menu(self):
        self.service_screen.validate_top_menu_is_present()

    #@pytest.allure.step("Validate instagram button is visible on the service page")
    #def test_service_screen_instagram(self):
        self.service_screen.validate_instagram_button_is_displayed()

    @pytest.allure.step("Validate the inPage title is visible on the service page")
    def test_service_screen_page_tile(self):
        self.service_screen.validate_page_title_is_visible()


    @pytest.allure.step("Validate the photo book design image s visible")
    def test_service_screen_photo_book_design_image_is_visible(self):
        self.service_screen.validate_photo_book_design_image()

    @pytest.allure.step("Validate that the social feed is available")
    def test_service_screen_social_feed(self):
        self.service_screen.validate_social_feed()

    @pytest.allure.step("Validate that the social feed is available")
    def test_service_screen_share_icons(self):
        self.service_screen.validate_share_icons()

    #@pytest.allure.step("Validate the photo book referral service image is visible ")
    #def test_service_screen_photo_referral_image(self):
    #    self.service_screen.validate_referral_service_image()



    def tearDown(self):
        self.driver.instance.quit()




if __name__ == '__main__':
    unittest.main()


