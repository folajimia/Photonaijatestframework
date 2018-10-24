from drivers.webdriver import Driver
import unittest
import pytest
import pyscreenshot
import allure
import os
import sys
sys.path.insert(0, '/users/jimiadekoya/pythonAutomationFramework')
from drivers.browserstack import BrowserStackDriver
from selenium import webdriver

#from drivers.browserstack import BrowserStackDriver
#from drivers import webdriver
#from selenium import Driver
from values import strings
from pageobjects import homescreen, servicescreen


##def driver():
##    return [Driver('safari'), Driver('chrome'), Driver('firefox')]
##
##def home_screen(driver)
##    home_screen = homescreen.HomeScreen(driver)
##    home_screen.click_service_screen_link()
##    return home_screen
#
#
#@pytest.allure.step("Validate Site title is visible")
#def test_home_screen_site_title(home_screen):
#    home_screen.validate_title_is_present()


class TestPhotoNaija(unittest.TestCase):

    def setUp(self):
        self.driver = Driver('chrome')
        self.driver.navigate(strings.base_url)
        self.home_screen = homescreen.HomeScreen(self.driver)
        self.home_screen.click_service_screen_link()
        self.service_screen = servicescreen.ServiceScreen(self.driver)
        #self.driver.

    @pytest.hookimpl(hookwrapper=True, tryfirst=True)
    def pytest_runtest_makereport(item, call):
        outcome = yield
        rep = outcome.get_result()
        setattr(item, "rep_" + rep.when, rep)
        return rep



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
        self.service_screen.validate_title_is_present()
        self.service_screen.validate_icon_is_present()
        self.service_screen.validate_top_menu_is_present()
        self.service_screen.validate_instagram_button_is_displayed()

    @pytest.allure.step("Validate the inPage title is visible on the service page")
    def test_service_screen_page_tile(self):
        try:
            self.service_screen.validate_page_title_is_visible()
        except AssertionError:
            print("failed assertion, screenshot take")
            self.driver.save_screenshot('error.png')




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


#class TestPhotoNaijaFirefox(TestPhotoNaija):
#    def setUp(self):
#        self.driver = Driver('firefox')
#        self.driver.navigate(strings.base_url)
#        self.home_screen = homescreen.HomeScreen(self.driver)
#        self.home_screen.click_service_screen_link()
#        self.service_screen = servicescreen.ServiceScreen(self.driver)
#
#    def tearDown(self):
#        self.driver.instance.quit()
#
#class TestPhotoNaijaIE(TestPhotoNaija):
#
#    def setUp(self):
#        self.driver = BrowserStackDriver('edge')
#        self.driver.navigate(strings.base_url)
#        self.home_screen = homescreen.HomeScreen(self.driver)
#        self.home_screen.click_service_screen_link()
#        self.service_screen = servicescreen.ServiceScreen(self.driver)
#        #self.driver.
#    def tearDown(self):
#        self.driver.instance.quit()




if __name__ == '__main__':
    unittest.main()


