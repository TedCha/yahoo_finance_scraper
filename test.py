import requests
from lxml import html
import pandas as pd
import math

def scrape_balance_sheet_data(stock):
    balance_sheet_url = f'https://finance.yahoo.com/quote/{stock}/balance-sheet'

    payload = {'p' : stock}

    response = requests.get(balance_sheet_url, params=payload)

    print(response.url)

    data = html.fromstring(response.text)

    balance_sheet_headers = data.xpath('//div[@class="D(tbhg)"]/div[1]/div')

    balance_sheet_data = data.xpath('//div[@data-test="fin-row"]/div[1]/div')

    header_row = [header.text_content() for header in balance_sheet_headers]

    data_uf = [data.text_content() for data in balance_sheet_data]

    data_array = [data_uf[5*i:5*i+5] for i in range(0,math.ceil(len(data_uf)/5))]

    balance_sheet_df = pd.DataFrame(data_array, columns=header_row)

    return balance_sheet_df