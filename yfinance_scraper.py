import requests
from lxml import html
import pandas as pd
import math
import sys
import xlsxwriter

from application import scrape_company_data

def main():
    stock = str(sys.argv[1])

    run = scrape_company_data(stock)

    summary_data = run.scrape_summary_data()

    profile_data = run.scrape_profile_data()

    income_statement = run.scrape_income_statement_data()

    file_name = './output/' + f'{stock} financial_report.xlsx'

    writer = pd.ExcelWriter(file_name, engine='xlsxwriter')

    summary_data.to_excel(writer, sheet_name='Summary', header=False)

    profile_data.to_excel(writer, sheet_name='Profile', index=False, header=False)

    income_statement.to_excel(writer, sheet_name='Income Statement', index=False)

    writer.save()

if __name__ == "__main__":
    main()