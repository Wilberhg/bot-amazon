from selenium.webdriver.chrome import options
import amazon.constants as const
import os
from selenium import webdriver
from amazon.amazon_filtration import AmazonFiltration

class Amazon(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += ';'+self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super().__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def enter_site(self):
        self.get(const.BASE_URL)

    def best_sellers(self):
        best_sellers = self.find_element_by_css_selector(
            'a[data-csa-c-content-id*="nav_cs_bestsellers"]'
            )
        best_sellers.click()

    def select_category(self):
        categories_element = self.find_element_by_css_selector(
            'div[class*="zg-browse-root"]'
            ).find_elements_by_tag_name(
                'a'
                )
        filtration = AmazonFiltration(driver=self)
        filtration.show_categories(categories_element)
        filtration.apply_category(categories_element)

    def report_results(self):
        results_elements = self.find_elements_by_class_name(
            'aok-inline-block.zg-item'
            )