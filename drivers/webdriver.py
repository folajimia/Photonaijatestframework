#import selenium
from selenium import webdriver
#System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver");
#WebDriver driver = new ChromeDriver();

class Driver:
    def __init__(self):
        self.instance = webdriver.Chrome()


    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
        else:
            raise TypeError("URL must be a string.")