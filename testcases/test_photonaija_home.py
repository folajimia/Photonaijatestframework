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


    def test_services_screen_components(self):
        home_screen = homescreen.HomeScreen(self.driver)
        home_screen.click_service_screen_link()

        service_screen = servicescreen.ServiceScreen(self.driver)
        service_screen.validate_title_is_present()
        service_screen.validate_icon_is_present()
        service_screen.validate_top_menu_is_present()
        service_screen.validate_instagram_button_is_displayed()


    def tearDown(self):
        self.driver.instance.quit()




if __name__ == '__main__':
    unittest.main()


