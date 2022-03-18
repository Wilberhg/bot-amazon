import amazon.constants as const
import os
from selenium import webdriver
from amazon.amazon_filtration import AmazonFiltration
from amazon.amazon_report import AmazonReport
import pyderman as dr
import warnings

warnings.filterwarnings("ignore")

class Amazon(webdriver.Chrome):
    def __init__(self, driver_path=const.MAIN_PATH+'\\driver', teardown=False):
        dr.install(dr.chrome, file_directory=rf'{driver_path}', overwrite=True, filename='chromedriver.exe', verbose=False)
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += ';'+self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super().__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, *args):
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
        category = filtration.apply_category(categories_element)
        return category

    def report_results(self):
        results_elements = self.find_elements_by_id(
            'gridItemRoot'
            )
        obj = AmazonReport(results_elements)
        products_list = obj.get_items_attributes()
        return products_list