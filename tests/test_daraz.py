import unittest
import time
from selenium import webdriver
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.product_page import ProductPage

class TestDarazFunctional(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(options=options)
        
    def test_complete_daraz_automation_flow(self):
        home_page = HomePage(self.driver)
        search_page = SearchPage(self.driver)
        product_page = ProductPage(self.driver)
        
        # Task 2: Navigate to Daraz.pk
        print("Opening Daraz.pk...")
        home_page.navigate("https://www.daraz.pk")
        time.sleep(4)  
        
        # Task 3: Search for "electronics"
        print("Searching for electronics...")
        home_page.search_for_item("electronics")
        time.sleep(4)
        
        # Tasks 4 & 5: Apply brand and price filters cleanly via URL parameters
        search_page.apply_brand_and_price_filters_via_url()
        
        # Task 6: Count products in results and validate > 0
        product_count = search_page.get_product_count()
        print(f"Total products found after filtering: {product_count}")
        self.assertTrue(product_count > 0, "Error: No products found on page matching this query!")
        print("Assertion Passed: Product count is greater than 0!")
        
        # Task 7: Open product details
        print("Opening the first product details...")
        search_page.click_first_product()
        time.sleep(4)
        
        # Switch contexts if opened in a new window tab
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])
        
        # Task 8: Verify if free shipping is available
        print("Verifying shipping options...")
        has_free_shipping = product_page.is_free_shipping_available()
        print(f"Is Free Shipping Available for this item? -> {has_free_shipping}")
        print("\n--- All Assignment Tasks Executed Successfully! ---")

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()