import unittest
from webdriver import Driver
from values import strings




class TestPhotoNaija(unittest.Testcase):

    def setUp(self):
        self.driver = Driver()
        self.driver.naviaget(strings.base_url)

        pass

    def test_home_screen_coonents(self):
        pass

    def tearDown(self):




if __name__ == '__main__':
    unittest.main()


