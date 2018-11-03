#import selenium
from selenium import webdriver
#System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver");
#System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver")
#WebDriver driver = new ChromeDriver();
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import WebDriverException
import os
import time
from datetime import datetime

class ErrorShots:

    def __init__(self):
        self.SCREEN_DUMP_LOCATION = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'screendumps')



    def take_screenshot(self,browser):
        filename = self._get_filename() +'.png'
        print('screenshotting to', filename)
        browser.get_screenshot_as_file(filename)

    def dump_html(self, browser):
        filename = self._get_filename() + '.html'
        print('dumping page HTML to', filename)
        with open(filename, 'w') as f:
            f.write(browser.page_source)

    def _get_filename(self):


        timestamp = datetime.now().isoformat().replace(':', '.')[:19]
        return '{folder}/{classname}.{method}-window{windowid}-{timestamp}'.format(
            folder=self.SCREEN_DUMP_LOCATION,
            classname=self.__class__.__name__,
            method=self._testMethodName,
            windowid=self.windowid,
            timestamp=timestamp
        )