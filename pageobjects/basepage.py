from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def validate_title_is_present(self):
        title = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.ID, "site-name")))
        assert title.is_displayed()
    def validate_icon_is_present(self):
        icon = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.ID, "logo")))
        assert icon.is_displayed()
    def validate_top_menu_is_present(self):
        top_menu = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.ID, "superfish-1")))
        assert top_menu.is_displayed()
    def validate_instagram_button_is_displayed(self):
        instagram_button = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "instagram")))
        assert instagram_button.is_displayed()

    def click_service_screen_link(self):
        service_screen_link = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "sf-depth-1")))
        assert service_screen_link.is_displayed()
        service_screen_link.click()
        


