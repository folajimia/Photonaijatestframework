import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:

    #@pytest.allure.step("Validate Site title is visible")
    def validate_title_is_present(self):
        title = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.ID, "site-name")))
        assert title.is_displayed()


    #@pytest.allure.step("Validate home icon is visible")
    def validate_icon_is_present(self):
        icon = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.ID, "logo")))
        assert icon.is_displayed()

    #@pytest.allure.step("Validate top menu is visible")
    def validate_top_menu_is_present(self):
        top_menu = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.ID, "superfish-1")))
        assert top_menu.is_displayed()

    #@pytest.allure.step("Validate instagram button is visible on home page")
    def validate_instagram_button_is_displayed(self):
        instagram_button = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "instagram")))
        assert instagram_button.is_displayed()


    # Top menu links
    def click_product_screen_link(self):
        product_screen_link = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.ID, "menu-1808-1")))
        product_screen_link_label = self.driver.instance.find_element_by_id("menu-1808-1").text
        assert product_screen_link.is_displayed()
        assert product_screen_link_label == 'PRODUCTS'
        product_screen_link.click()


    def click_prices_screen_link(self):
        prices_screen_link = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.ID, "menu-1823-1")))
        prices_screen_link_label = self.driver.instance.find_element_by_id("menu-1823-1").text
        assert prices_screen_link.is_displayed()
        assert prices_screen_link_label == 'PRICES'
        prices_screen_link.click()

    def click_faq_screen_link(self):
        faq_screen_link = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.ID, "menu-1810-1")))
        faq_screen_link_label = self.driver.instance.find_element_by_id("menu-1810-1").text
        assert faq_screen_link.is_displayed()
        assert faq_screen_link_label == 'FAQ'
        faq_screen_link.click()


    def click_contact_screen_link(self):
        contact_screen_link = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.ID, "menu-442-1")))
        contact_screen_link_label = self.driver.instance.find_element_by_id("menu-442-1").text
        assert contact_screen_link.is_displayed()
        assert contact_screen_link_label == 'CONTACT'
        contact_screen_link.click()

    def click_login_screen_link(self):
        login_screen_link = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.ID, "menu-1811-1")))
        login_screen_link_label = self.driver.instance.find_element_by_id("menu-1811-1").text
        assert login_screen_link.is_displayed()
        assert login_screen_link_label == 'LOGIN'
        login_screen_link.click()

    def click_service_screen_link(self):
        service_screen_link = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.ID, "menu-1809-1")))
        service_screen_link_label = self.driver.instance.find_element_by_id("menu-1809-1").text
        assert service_screen_link.is_displayed()
        assert service_screen_link_label == 'SERVICES'
        service_screen_link.click()




