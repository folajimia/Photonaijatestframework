

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

        # self.photo_book_design_image = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="block-system-main"]/div/div/div/div[1]/div[1]/div/div/a/img')))
        # self.referral_service_image = WebDriverWait(self.driver.instance,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="block-system-main"]/div/div/div/div[2]/div[1]/div/div/a/img')))

 #def validate_photo_book_design_image(self):
    #    assert self.photo_book_design_image.is_displayed()

    #def validate_referral_service_image(self):
     #   assert self.referral_service_image.is_displayed()