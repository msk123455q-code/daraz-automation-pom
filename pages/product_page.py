from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException

class ProductPage(BasePage):
    """Handles verification steps inside the specific product's details page."""
    
    # LOCATOR: Looks for text mentions of 'Free Shipping' in the delivery details box
    SHIPPING_INFO = (By.XPATH, "//*[contains(text(), 'Free Shipping') or contains(text(), 'Free shipping')]")

    def is_free_shipping_available(self):
        """Returns True if the Free Shipping banner/text is found within 10 seconds, else False."""
        try:
            self.wait.until(lambda d: d.find_element(*self.SHIPPING_INFO))
            return True
        except TimeoutException:
            return False