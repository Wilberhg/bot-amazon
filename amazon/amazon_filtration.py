from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class AmazonFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.contador = 0
        self.opcoes = {}

    def show_categories(self, categories_elements):
        for opcao in categories_elements:
            self.contador+=1
            self.opcoes[self.contador] = opcao.text

        for k, v in self.opcoes.items():
            print(k, '-', v.strip())

    def apply_category(self, categories_elements):
        while True:
            try:
                opcao = int(input('\nQual o número da categoria você deseja explorar?\nR:'))
                if opcao > len(self.opcoes):
                    print(f'\nPor favor, insira um número menor que {len(self.opcoes)+1}!')
                    continue
                break
            except TypeError:
                print('\nPor favor, insira um número válido!\n')
                continue

        print(f'\nVocê selecionou a opção "{self.opcoes[opcao].strip()}"\n')

        for element in categories_elements:
            if self.opcoes[opcao] in element.text:
                element.click()
                break

        return self.opcoes[opcao].strip()