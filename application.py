import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import time

class scrape_summary_data():

    def __init__(self, stock):
        self.stock = stock

    def scrape_summary_data(self):
        summary_url = f'https://finance.yahoo.com/quote/{self.stock}'

        payload = {'p' : self.stock}

        response = requests.get(summary_url, params=payload)

        data = response.text

        soup = BeautifulSoup(data, 'lxml')

        company_name = soup.select("#div.D(ib)")

        summary_data = soup.select("#quote-summary tr")

        company_summary_dict = dict()
        
        company_summary_dict['company'] = company_name

        company_summary_dict['stock'] = self.stock

        for i in range(len(summary_data)): 
            rows = [row.text for row in summary_data[i]]
            key = rows[0]
            value = rows[1]

            # Add a value to our class_dict dictionary
            company_summary_dict[str(key)] = str(value)
        
        return company_summary_dict

class scrape_profile_data():

    def __init__(self, stock):
        self.stock = stock

    def scrape_profile_data(self):
        profile_url = f'https://finance.yahoo.com/quote/{self.stock}/profile'

        payload = {'p' : self.stock}

        response = requests.get(profile_url, params=payload)

        data = response.text

        soup = BeautifulSoup(data, 'lxml')

        profile_data = soup.select('#asset-profile-container p')

        company_profile_dict = dict()

        for i in range(len(profile_data)): 
            rows = [row.text for row in profile_data[i]]
            key = rows[0]
            value = rows[1]

            # Add a value to our class_dict dictionary
            company_profile_dict[str(key)] = str(value)
        
        return company_profile_dict

class scrape_financials_data():

    def __init__(self, stock):
        self.stock = stock

    def scrape_financials_data(self):
        financials_url = f'https://finance.yahoo.com/quote/{self.stock}/financials'

        payload = {'p' : self.stock}

        response = requests.get(financials_url, params=payload)

        data = response.text

        soup = BeautifulSoup(data, 'lxml')

        financials_data = soup.select('div.Pos(r)')

        company_financials_dict = dict()

        for i in range(len(financials_data)): 
            rows = [row.text for row in financials_data[i]]
            key = rows[0]
            value = rows[1]

            # Add a value to our class_dict dictionary
            company_financials_dict[str(key)] = str(value)
        
        return company_financials_dict

        