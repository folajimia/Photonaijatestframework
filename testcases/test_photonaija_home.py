import unittest
from webdriver import Driver
from values import strings
from pageobjects import HomeScreen




class TestPhotoNaija(unittest.Testcase):

    def setUp(self):
        self.driver = Driver()
        self.driver.naviaget(strings.base_url)

        pass

    def test_home_screen_components(self):
        home_screen = HomeScreen(self.driver)
        home_screen.validate_title_is_present()
        home_screen.validate_icon_is_present()
        home_screen.validate_menu_options_are_present()
        home_screen.validdate_posts_are_visible()
        home_screen.validate_social_media_links()
        pass

    def tearDown(self):
        self.driver.instance.quit()




if __name__ == '__main__':
    unittest.main()


