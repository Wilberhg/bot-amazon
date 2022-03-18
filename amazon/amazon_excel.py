from datetime import date
import amazon.constants as const
import os
import xlsxwriter 

class AmazonExcel:
    def __init__(self, filename):
        os.makedirs(f'{const.MAIN_PATH}\\files', exist_ok=True)
        self.filename = filename.replace(' ', '_')
        self._today_date = date.today().strftime('%d_%m_%Y')
        self._wb = xlsxwriter.Workbook(fr'{const.MAIN_PATH}\files\{self.filename}_{self._today_date}.xlsx')

    def create_layout(self):
        self._ws = self._wb.add_worksheet()
        bold = self._wb.add_format({'bold':1})
        self._ws.write('A1','Nome do produto', bold)
        self._ws.write('B1','Nota do produto', bold)
        self._ws.write('C1','Valor do produto', bold)

    def write_results(self, products):
        row = 1
        col = 0
        for obj in products:
            self._ws.write_string(row, col, obj['nome'])
            self._ws.write_string(row, col+1, obj['nota'])
            self._ws.write_string(row, col+2, obj['valor'])
            row+=1

    def save_and_close(self):
        self._wb.close()