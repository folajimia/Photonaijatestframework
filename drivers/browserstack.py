from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from browserstack.local import Local
import os, json
import pytest



class BrowserStackDriver:

    def __init__(self, browser_type):
        desired_cap = {
            'browser': 'Edge',
            'browser_version': '16.0',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1024x768'
        }
        USERNAME = 'username'
        PASSWORD = 'access'

        if browser_type.lower() == 'edge':
            self.instance = webdriver.Remote(
                command_executor='http://%s:%s@hub.browserstack.com:80/wd/hub' % (USERNAME, PASSWORD),
                desired_capabilities=desired_cap)



# We do not use this code at clients
# We use Driver_Factory to return apporpriate drivers within our framework
    #def __init__(self, browser, browser_version, platform, os_version):
    #    "Run the test in browser stack browser stack flag is 'Y'"
    #    USERNAME = 'jimi.adekoya@mheducation.com'  # We fetch values from a conf file in our framework we use on our clients
    #    PASSWORD = 'Test1234!'
    #    if browser.lower() == 'firefox':
    #        self.desired_capabilities = DesiredCapabilities.FIREFOX
    #    if browser.lower() == 'edge':#
    #        self.desired_capabilities = DesiredCapabilities.EDGE
    #    if browser.lower() == 'ie':
    #        self.desired_capabilities = DesiredCapabilities.INTERNETEXPLORER
    #    self.desired_capabilities['os'] = 'Windows'
    #    self.desired_capabilities['os_version'] = '10'
    #    self.desired_capabilities['browser_version'] = '16.0'
    #    self.desired_capabilities['resolution'] = '1024x768'
        #Todo create a config file to store access  details

        #return webdriver.Remote(command_executor='http://%s:%s@hub.browserstack.com:80/wd/hub' % (USERNAME, PASSWORD),
         #                   desired_capabilities = self.desired_capabilities)


    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
        else:
            raise TypeError("URL must be a string.")