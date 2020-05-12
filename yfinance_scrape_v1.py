import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import time

timestr = time.strftime("%Y-%m-%d %H-%M-%S")

outfile_name = 'yfinance_scrape ' + timestr + '.csv'

with open('companies.csv', 'r', encoding='utf8') as file:
    reader = csv.DictReader(file)
    out_dict = {}
    for row in reader:
        for column, value in row.items():
            out_dict.setdefault(str(column).strip(), []).append(str(value).strip())

for i in range(len(out_dict['company'])):
    if out_dict['stock'][i] == 'PRIVATE':
        pass
    else:
        stock = out_dict['stock'][i]
        payload = {'p' : stock}

        url = f'https://finance.yahoo.com/quote/{stock}'
        
        response = requests.get(url, params=payload)

        data = response.text

        soup = BeautifulSoup(data, 'lxml')

        finance_data = soup.select("#quote-summary tr")

        company_finance_dict = dict()
        
        company_finance_dict['company'] = out_dict['company'][i]

        company_finance_dict['stock'] = out_dict['stock'][i]

        for i in range(len(finance_data)): 
            rows = [row.text for row in finance_data[i]]
            key = rows[0]
            value = rows[1]

            # Add a value to our class_dict dictionary
            company_finance_dict[str(key)] = str(value)

        with open(outfile_name, 'a', newline='', encoding='utf8') as file:
            writer = csv.DictWriter(file, company_finance_dict.keys())
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(company_finance_dict)


