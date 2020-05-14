import pandas as pd
import sys
import xlsxwriter

from application import scrape_company_data

def main():

    # --- Input and Setup --- #

    stock = str(input('Ticker Symbol: '))

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:77.0) Gecko/20100101 Firefox/77.0'}

    # --- Class Instance Creation --- #

    run = scrape_company_data(stock, headers)

    # --- Scrape Methods Execution --- #

    summary_data = run.scrape_summary_data()

    profile_data = run.scrape_profile_data()

    income_statement = run.scrape_income_statement_data()

    balance_sheet = run.scrape_balance_sheet_data()

    cash_flow = run.scrape_cash_flow_data()

    # --- Record Data to XLSX --- #

    file_name = './output/' + f'{stock}_financial_report.xlsx'

    writer = pd.ExcelWriter(file_name, engine='xlsxwriter')

    summary_data.to_excel(writer, sheet_name='Summary', header=False)

    profile_data.to_excel(writer, sheet_name='Profile', index=False, header=False)

    income_statement.to_excel(writer, sheet_name='Income_Statement', index=False)

    balance_sheet.to_excel(writer, sheet_name='Balance_Sheet', index=False)

    cash_flow.to_excel(writer, sheet_name='Cash_Flow', index=False)

    # --- Save Data --- #

    writer.save()

if __name__ == "__main__":
    main()