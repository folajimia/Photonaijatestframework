from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os, json
import pytest



class BrowserStackDriver:

    def __init__(self, browser_type):
        #desired_cap = {
        #    'browser': 'Edge',
        #    'browser_version': '16.0',
        #    'os': 'Windows',
        #    'os_version': '10',
        #    'resolution': '1024x768'
        #}
        USERNAME = username
        PASSWORD = password

        if browser_type.lower() == 'edge':
            self.instance = webdriver.Remote(
                command_executor='http://%s:%s@hub.browserstack.com:80/wd/hub' % (USERNAME, PASSWORD),
                desired_capabilities=DesiredCapabilities.EDGE)
        if browser_type.lower() == 'ie':
            self.instance = webdriver.Remote(
                command_executor='http://%s:%s@hub.browserstack.com:80/wd/hub' % (USERNAME, PASSWORD),
                desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
        else:
            raise TypeError("URL must be a string.")