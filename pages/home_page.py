from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class HomePage(BasePage):
    # Standard Daraz Search input field ID
    SEARCH_INPUT = (By.ID, "q")

    def search_for_item(self, item_name):
        self.type_text(self.SEARCH_INPUT, item_name)
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(Keys.ENTER)