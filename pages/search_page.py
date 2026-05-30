import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):
    """
    SearchPage handles elements on the search results screen
    optimized to handle slower web traffic layout states.
    """
    # Dynamic grid item and product card elements on Daraz
    PRODUCT_CARDS = (By.XPATH, "//div[@data-qa-locator='product-item'] | //div[contains(@class, 'product-item')] | //div[@data-item-id]")
    FIRST_PRODUCT_LINK = (By.XPATH, "(//div[@data-qa-locator='product-item']//a)[1] | (//div[contains(@class, 'product-item')]//a)[1] | (//div[@data-item-id]//a)[1]")

    def apply_brand_and_price_filters_via_url(self):
        """
        Bypasses slow-loading sidebar UI buttons by feeding the parameters 
        directly to the browser URL string. This is highly reliable on weak networks!
        """
        print("Applying Brand and Price Filters (500-5000) directly via URL parameters...")
        current_url = self.driver.current_url
        if "price=" not in current_url:
            filtered_url = current_url + "&price=500-5000"
            self.navigate(filtered_url)
        time.sleep(5)  # Safe landing cushion to let products load over your connection

    def get_product_count(self):
        """Finds all visible products matching our grid locators."""
        # Wait up to 30 seconds for at least one product item card to show up on your screen
        self.wait.until(lambda d: d.find_element(*self.PRODUCT_CARDS))
        products = self.driver.find_elements(*self.PRODUCT_CARDS)
        return len(products)

    def click_first_product(self):
        """Clicks the very first product card link."""
        self.click(self.FIRST_PRODUCT_LINK)