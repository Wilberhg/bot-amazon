from datetime import date
import xlsxwriter 

class AmazonExcel(xlsxwriter):
    def __init__(self):
        self.today_date = date.today().strftime('%d_%m_%Y')
        super().__init__()

    def extract_result(self):
        wb = self.Workbook(fr'')
