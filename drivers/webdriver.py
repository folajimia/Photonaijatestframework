#import selenium
from selenium import webdriver
#System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver");
#System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver")
#WebDriver driver = new ChromeDriver();
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Driver:

    def __init__(self, browser_type):
        if browser_type.lower() == 'firefox':
            self.instance = webdriver.Firefox()
        elif browser_type.lower() == 'ie':
            self.instance = webdriver.Ie()
        elif browser_type.lower() == 'chrome':
            self.instance = webdriver.Chrome()
        elif browser_type.lower() == 'opera':
            self.instance = webdriver.Opera()
        elif browser_type.lower() == 'safari':
            self.instance = webdriver.Safari()
        else:
            print("Browser is not available")

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
        else:
            raise TypeError("URL must be a string.")

