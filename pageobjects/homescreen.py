from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from values import strings



class HomeScreen():

    def __init__(self, driver):
        self.driver = driver
        self.title = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.ID, "site-name")))
        self.icon = WebDriverWait(self.driver.instance,10).until(EC.visibility_of_element_located((By.ID, "logo")))
        self.top_menu = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.ID, "superfish-1")))
        #self.post_list = WebDriverWait(self.driver.instance, 10).until((EC.visibility_of_element_located(By.TAG_NAME, "article")))
        self.instagram_button = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "instagram")))
        #self.linked_button = WebDriverWait(self.driver.instance,10).until((EC.visibility_of_element_located(By.XPATH,"")))

    def validate_title_is_present(self):
        assert self.title.is_displayed()
    def validate_icon_is_present(self):
        assert self.icon.is_displayed()
    def validate_top_menu_is_present(self):
        assert self.top_menu.is_displayed()
    def validate_instagram_button_is_displayed(self):
        assert self.instagram_button.is_displayed()
        #def validate_linked_button_is_displayed(self)
        #    assert self.linked_button.is_dispalyed()
        # def validate_post_list_is_present(self):
        # assert self.post_list.is_displayed()