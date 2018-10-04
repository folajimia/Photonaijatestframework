import pytest
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



from pageobjects.homescreen import HomeScreen
from pageobjects.basepage import BasePage


class ServiceScreen(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.page_title = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.ID, "page-title")))

    @pytest.allure.step("Validate page title is visible")
    def validate_page_title_is_visible(self):
        assert self.page_title.is_displayed()





