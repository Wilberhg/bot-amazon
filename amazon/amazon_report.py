class AmazonReport:
    def __init__(self, result_elements):
        self.result_elements = result_elements

    def get_items_attributes(self):
        products = []
        for item in self.result_elements:
            nome = item.find_element_by_tag_name('img').get_attribute('alt')
            nota = item.find_element_by_css_selector('a[title*="estrela"]').get_attribute('title')
            try:
                valor = item.find_element_by_class_name('a-size-base.a-color-price').text
            except:
                valor = 'Não disponivel'
            products.append({'nome':nome,'nota':nota,'valor':valor})
        return products