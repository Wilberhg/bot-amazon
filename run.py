from amazon.amazon import Amazon
from amazon.amazon_excel import AmazonExcel

try:
    with Amazon() as bot:
        bot.enter_site()
        bot.best_sellers()
        category = bot.select_category()
        products_list = bot.report_results()
    excel = AmazonExcel(category)
    excel.create_layout()
    excel.write_results(products_list)
    excel.save_and_close()
except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise