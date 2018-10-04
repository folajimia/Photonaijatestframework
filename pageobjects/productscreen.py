

class ProductScreen:

    def __init__(self, driver):
        self.driver = driver





    def test_services_screen_components(self):
        home_screen = HomeScreen(self.driver)
        home_screen.click_service_product_link()

        product_screen = ProductScreen(self.driver)
        product_screen.validate_title_is_present()
        product_screen.validate_icon_is_present()
        product_screen.validate_top_menu_is_present()
        product_screen.validate_instagram_button_is_displayed()