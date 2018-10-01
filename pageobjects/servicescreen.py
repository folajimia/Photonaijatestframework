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

        self.product_bar = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_all_elements_located((By.ID, "block-views-showcases-block-2")))

    @pytest.allure.step("Validate product bar is visible")
    def validate_product_bar_is_visible(self):
        assert (self.product_bar) > 0





    def test_services_screen_components(self):
        home_screen = HomeScreen(self.driver)
        home_screen.click_service_screen_link()

        service_screen = ServiceScreen(self.driver)
        service_screen.validate_title_is_present()
        service_screen.validate_icon_is_present()
        service_screen.validate_top_menu_is_present()
        service_screen.validate_instagram_button_is_displayed()