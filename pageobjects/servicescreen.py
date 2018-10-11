import pytest
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from drivers.webdriver import Driver
from selenium import webdriver



from pageobjects.homescreen import HomeScreen
from pageobjects.basepage import BasePage


class ServiceScreen(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.page_title = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.ID, "page-title")))
        self.page_title_label = self.driver.instance.find_element_by_id("page-title").text
        self.photo_book_design_image = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="block-system-main"]/div/div/div/div/div[1]/div/div/a/img')))
        self.photo_book_design_link = WebDriverWait(self.driver.instance,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#block-system-main > div > div > div > div > div.views-field.views-field-title > h2 > a')))
        self.photo_book_design_explain = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="block-system-main"]/div/div/div/div/div[3]/div/p')))
        self.photo_book_design_price = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="block-system-main"]/div/div/div/div/div[4]/div')))
        self.photo_book_design_read_more_button = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="block-system-main"]/div/div/div/div/div[5]/span/a')))
        self.social_feed = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'instagram-social-feed')))

        self.share_icon_facebook = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'st_facebook_large')))
        self.share_icon_twitter = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'st_twitter_large')))
        self.share_icon_pinterest = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'st_pinterest_large')))
        self.share_icon_googleplus = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'st_googleplus_large')))
        self.share_icon_tumblr = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'st_tumblr_large')))
        self.share_icon_sharethis = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'st_sharethis_large')))

        #self.photo_book_design_label = self.driver.instance.find_element_by_id("page-title").text
        print(self.photo_book_design_price.text)


    #@pytest.allure.step("Validate page title is visible")
    def validate_page_title_is_visible(self):
        assert self.page_title.is_displayed()
        assert self.page_title_label == 'SERVICES'
        #assert self.page_title.

    def validate_photo_book_design_image(self):
        assert self.photo_book_design_image.is_displayed()
        assert self.photo_book_design_link.is_displayed()
        assert self.photo_book_design_explain.is_displayed()
        assert self.photo_book_design_price.is_displayed()
        assert self.photo_book_design_read_more_button.is_displayed()

        assert self.photo_book_design_link.text == 'PHOTOBOOK DESIGN'
        assert self.photo_book_design_explain.text == 'Not experienced in Photobook designs or simply too busy to handle that task ? Photonaija can help...'
        #assert self.photo_book_design_price.text == '₦10,000.00'
        assert self.photo_book_design_read_more_button.text == 'READ MORE'

    def validate_social_feed(self):
        assert self.social_feed.is_displayed()

    def validate_share_icons(self):
        assert self.share_icon_facebook.is_displayed()
        assert self.share_icon_twitter.is_displayed()
        assert self.share_icon_pinterest.is_displayed()
        assert self.share_icon_googleplus.is_displayed()
        assert self.share_icon_tumblr.is_displayed()
        assert self.share_icon_sharethis.is_displayed()






