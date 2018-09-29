import unittest
from drivers.webdriver import Driver
#from drivers import webdriver
#from selenium import Driver
from values import strings
from pageobjects import homescreen




class TestPhotoNaija(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_home_screen_components(self):
        home_screen = homescreen.HomeScreen(self.driver)
        home_screen.validate_title_is_present()
        home_screen.validate_icon_is_present()
        home_screen.validate_menu_options_are_present()
        home_screen.validdate_posts_are_visible()
        home_screen.validate_social_media_links()


    def tearDown(self):
        self.webdriver.driver.instance.quit()




if __name__ == '__main__':
    unittest.main()


