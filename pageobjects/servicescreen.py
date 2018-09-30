from pageobjects.homescreen import HomeScreen
from pageobjects.basepage import BasePage


class ServiceScreen(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def test_services_screen_components(self):
        home_screen = HomeScreen(self.driver)
        home_screen.click_service_screen_link()

        service_screen = ServiceScreen(self.driver)
        service_screen.validate_title_is_present()
        service_screen.validate_icon_is_present()
        service_screen.validate_top_menu_is_present()
        service_screen.validate_instagram_button_is_displayed()