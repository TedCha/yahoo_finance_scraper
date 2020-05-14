import pandas as pd
import sys
import xlsxwriter

from application import scrape_company_data

def main():

    # --- Call scraping functions and perform web scrape. --- #

    stock = str(input('Stock Symbol: '))

    run = scrape_company_data(stock)

    summary_data = run.scrape_summary_data()

    profile_data = run.scrape_profile_data()

    income_statement = run.scrape_income_statement_data()

    balance_sheet = run.scrape_balance_sheet_data()

    cash_flow = run.scrape_cash_flow_data()

    # --- Write scraped data to xlsx file. --- #

    file_name = './output/' + f'{stock}_financial_report.xlsx'

    writer = pd.ExcelWriter(file_name, engine='xlsxwriter')

    summary_data.to_excel(writer, sheet_name='Summary', header=False)

    profile_data.to_excel(writer, sheet_name='Profile', index=False, header=False)

    income_statement.to_excel(writer, sheet_name='Income_Statement', index=False)

    balance_sheet.to_excel(writer, sheet_name='Balance_Sheet', index=False)

    cash_flow.to_excel(writer, sheet_name='Cash_Flow', index=False)

    writer.save()

if __name__ == "__main__":
    main()