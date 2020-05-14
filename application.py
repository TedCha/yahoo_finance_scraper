import requests
from lxml import html
import pandas as pd
import xlsxwriter
import math
from tkinter import filedialog, Tk

class scrape_company_data():


    # --- Initialize Instance Variables --- #

    def __init__(self, stock, user_agent):
        self.stock = stock
        self.user_agent = user_agent

    # --- Scrape Company Summary Data --- #

    def scrape_summary_data(self):
        summary_url = f'https://finance.yahoo.com/quote/{self.stock}'

        payload = {'p' : self.stock}

        response = requests.get(summary_url, params=payload, headers=self.user_agent)

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

        df_i = pd.DataFrame([summary_data_str], columns=summary_data_header_str)

        summary_data_df = df_i.transpose()

        print(self.stock + ' Financial Summary Data Scraped')

        return summary_data_df


    # --- Scrape Company Profile Data --- #

    def scrape_profile_data(self):
        profile_url = f'https://finance.yahoo.com/quote/{self.stock}/profile'

        payload = {'p' : self.stock}

        response = requests.get(profile_url, params=payload, headers=self.user_agent)

        data = html.fromstring(response.text)

        profile_data = data.xpath('//*[@class="Mb(25px)"]/p[2]/span')

        profile_data_str = [profile.text_content() for profile in profile_data]

        df_i = pd.DataFrame([profile_data_str[0::2], profile_data_str[1::2]])

        profile_data_df = df_i.transpose()

        print(self.stock + ' Company Profile Data Scraped')

        return profile_data_df

    
    # --- Scrape Company Income Statement Data --- #
    
    def scrape_income_statement_data(self):
        income_statement_url = f'https://finance.yahoo.com/quote/{self.stock}/financials'

        payload = {'p' : self.stock}

        response = requests.get(income_statement_url, params=payload, headers=self.user_agent)

        data = html.fromstring(response.text)

        income_statement_headers = data.xpath('//*[@class="D(tbhg)"]/div[1]/div')

        income_statement_rows = data.xpath('//*[@data-test="fin-row"]/div[1]/div')

        header_row = [header.text_content() for header in income_statement_headers]

        data_uf = [data.text_content() for data in income_statement_rows]

        j = len(data.xpath('//*[@class="D(tbr) C($primaryColor)"]/div'))

        data_array = [data_uf[j*i:j*i+j] for i in range(0,math.ceil(len(data_uf)/j))]

        income_statement_df = pd.DataFrame(data_array, columns=header_row)

        print(self.stock + ' Income Statement Data Scraped')

        return income_statement_df

    
    # --- Scrape Company Balance Sheet Data --- #

    def scrape_balance_sheet_data(self):
        balance_sheet_url = f'https://finance.yahoo.com/quote/{self.stock}/balance-sheet'

        payload = {'p' : self.stock}

        response = requests.get(balance_sheet_url, params=payload, headers=self.user_agent)

        data = html.fromstring(response.text)

        balance_sheet_headers = data.xpath('//div[@class="D(tbhg)"]/div[1]/div')

        balance_sheet_data = data.xpath('//div[@data-test="fin-row"]/div[1]/div')

        header_row = [header.text_content() for header in balance_sheet_headers]

        data_uf = [data.text_content() for data in balance_sheet_data]

        j = len(data.xpath('//*[@class="D(tbr) C($primaryColor)"]/div'))

        data_array = [data_uf[j*i:j*i+j] for i in range(0,math.ceil(len(data_uf)/j))]

        balance_sheet_df = pd.DataFrame(data_array, columns=header_row)

        print(self.stock + ' Balance Sheet Data Scraped')

        return balance_sheet_df

    
    # --- Scrape Company Cash Flow Data --- #
    
    def scrape_cash_flow_data(self):
        balance_sheet_url = f'https://finance.yahoo.com/quote/{self.stock}/cash-flow'

        payload = {'p' : self.stock}

        response = requests.get(balance_sheet_url, params=payload, headers=self.user_agent)

        data = html.fromstring(response.text)

        cash_flow_headers = data.xpath('//div[@class="D(tbhg)"]/div[1]/div')

        cash_flow_data = data.xpath('//div[@data-test="fin-row"]/div[1]/div')

        header_row = [header.text_content() for header in cash_flow_headers]

        data_uf = [data.text_content() for data in cash_flow_data]

        j = len(data.xpath('//*[@class="D(tbr) C($primaryColor)"]/div'))

        data_array = [data_uf[j*i:j*i+j] for i in range(0,math.ceil(len(data_uf)/j))]

        cash_flow_df = pd.DataFrame(data_array, columns=header_row)

        print(self.stock + ' Cash Flow Data Scraped')

        return cash_flow_df


    # --- Scrape Company Statistics Data --- #

    def scrape_valuation_measures_data(self):

        statistics_url = f'https://finance.yahoo.com/quote/{self.stock}/key-statistics'

        payload = {'p' : self.stock}

        response = requests.get(statistics_url, params=payload, headers=self.user_agent)

        data = html.fromstring(response.text)

        valuation_measures_headers = data.xpath('//*[@class="Bdtw(0px) C($primaryColor)"]/th/span')
    
        valuation_measures_data = data.xpath('//*[@class="W(100%) Bdcl(c)  M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"]/tbody/tr/td')

        header_row = [header.text_content() for header in valuation_measures_headers]

        data_uf = [data.text_content() for data in valuation_measures_data]

        header_row.pop(0)

        header_row.insert(0, 'Measure')

        header_row.insert(1, 'Current')

        j = len(valuation_measures_headers) + 1

        data_array = [data_uf[j*i:j*i+j] for i in range(0,math.ceil(len(data_uf)/j))]

        valuation_measures_df = pd.DataFrame(data_array, columns=header_row)

        print(self.stock + ' Valuation Measures Data Scraped')

        return valuation_measures_df


class application_methods:

    @staticmethod
    def load_input_data():
        root = Tk()
        root.attributes("-topmost", True)
        root.withdraw()
        file_name = filedialog.askopenfilename(title='Select Input File')

        with open(file_name, 'r', encoding='utf8') as f:
            stocks = [line.strip() for line in f]

        root.destroy()
        
        return stocks
    
    @staticmethod
    def select_output_directory():
        root = Tk()
        root.attributes("-topmost", True)
        root.withdraw()
        directory_path = filedialog.askdirectory(title='Select Output Folder')

        return directory_path
    
    @staticmethod
    def write_xlsx_file(stock,
    output_directory,
    summary_data, 
    profile_data, 
    income_statement,
    balance_sheet, 
    cash_flow, 
    valuation_measures):

        file_name = output_directory + f'/{stock}_financial_report.xlsx'

        writer = pd.ExcelWriter(file_name, engine='xlsxwriter')

        summary_data.to_excel(writer, sheet_name='Summary', header=False)

        profile_data.to_excel(writer, sheet_name='Profile', index=False, header=False)

        income_statement.to_excel(writer, sheet_name='Income_Statement', index=False)

        balance_sheet.to_excel(writer, sheet_name='Balance_Sheet', index=False)

        cash_flow.to_excel(writer, sheet_name='Cash_Flow', index=False)

        valuation_measures.to_excel(writer, sheet_name='Valuation_Measures', index=False)

        # --- Save Data --- #

        writer.save()


    

        