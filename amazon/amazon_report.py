class AmazonReport:
    def __init__(self, result_elements):
        self.result_elements = result_elements

    def get_items_attributes(self):
        products = []
        for item in self.result_elements:
            nome = item.find_element_by_class_name('p13n-sc-truncated').text
            nota = item.find_elements_by_class_name('a-link-normal')[1].get_attribute('title')
            try:
                valor = item.find_element_by_class_name('a-size-base.a-color-price').text
            except:
                valor = 'Não disponivel'
            products.append({'nome':nome,'nota':nota,'valor':valor})
        return products