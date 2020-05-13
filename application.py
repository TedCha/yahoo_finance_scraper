import requests
from lxml import html
import csv
import pandas as pd
import math

class scrape_company_data():

    def __init__(self, stock):
        self.stock = stock

    def scrape_summary_data(self):
        summary_url = f'https://finance.yahoo.com/quote/{self.stock}'

        payload = {'p' : self.stock}

        response = requests.get(summary_url, params=payload)

        data = html.fromstring(response.text)

        company_name = data.xpath('//*[@class="Mt(15px)"]/div[1]/div[1]/h1')

        summary_data_headers = data.xpath('//*[@id="quote-summary"]/div/table/tbody/tr/td[1]')

        summary_data = data.xpath('//*[@id="quote-summary"]/div/table/tbody/tr/td[2]')

        company_name_list = [name.text_content() for name in company_name]

        company_name_str = company_name_list[0]

        summary_data_header_str  = [header.text_content() for header in summary_data_headers]

        summary_data_str  = [data.text_content() for data in summary_data]

        summary_data_header_str.insert(0, 'Company')

        summary_data_str.insert(0, company_name_str)

        summary_data_df = pd.DataFrame([summary_data_str], columns=summary_data_header_str)

        print(summary_data_df)

    def scrape_profile_data(self):
        profile_url = f'https://finance.yahoo.com/quote/{self.stock}/profile'

        payload = {'p' : self.stock}

        response = requests.get(profile_url, params=payload)

        data = html.fromstring(response.text)

        profile_data = data.xpath('//*[@class="D(ib) Va(t)"]/span')

        profile_data_str = [profile.text_content() for profile in profile_data]

        profile_data_df = pd.DataFrame([profile_data_str[1::2]], columns=profile_data_str[0::2])

        print(profile_data_df)
    
    def scrape_income_statement_data(self):
        income_statement_url = f'https://finance.yahoo.com/quote/{self.stock}/financials'

        payload = {'p' : self.stock}

        response = requests.get(income_statement_url, params=payload)

        data = html.fromstring(response.text)

        income_statement_headers = data.xpath('//*[@class="D(tbhg)"]/div[1]/div')

        income_statement_rows = data.xpath('//*[@data-test="fin-row"]/div[1]/div')

        header_row = [header.text_content() for header in income_statement_headers]

        data_uf = [data.text_content() for data in income_statement_rows]

        data_array = [data_uf[6*i:6*i+6] for i in range(0,math.ceil(len(data_uf)/6))]

        income_statement_df = pd.DataFrame(data_array, columns=header_row)

        print(income_statement_df)

    

        