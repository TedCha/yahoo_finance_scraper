import pandas as pd
import sys
import time

from application import scrape_company_data, application_methods

def main():

    print('Once the window opens, please load the stock ticker file.')

    time.sleep(1)

    stocks = application_methods.load_input_data()

    print('Once the window opens, please load the output directory.\n')

    time.sleep(1)

    output_directory = application_methods.select_output_directory()

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:77.0) Gecko/20100101 Firefox/77.0'}

    for i in range(len(stocks)):

        stock = stocks[i]

        # --- Class Instance Creation --- #

        run = scrape_company_data(stock, headers)

        # --- Scrape Methods Execution --- #

        summary_data = run.scrape_summary_data()
        profile_data = run.scrape_profile_data()
        income_statement = run.scrape_income_statement_data()
        balance_sheet = run.scrape_balance_sheet_data()
        cash_flow = run.scrape_cash_flow_data()
        valuation_measures = run.scrape_valuation_measures_data()

        misc_data = run.scrape_highlights_and_trading_data()
        highlight_data = misc_data['financial']
        trading_data = misc_data['trading']

        # --- Record Data to XLSX File --- #

        application_methods.write_xlsx_file(stock, 
        output_directory, 
        summary_data, profile_data, 
        income_statement, 
        balance_sheet, 
        cash_flow, 
        valuation_measures,
        highlight_data,
        trading_data)

        print(stock + ' Report Written')
        print('------------------------------------')

        time.sleep(2)

if __name__ == "__main__":
    start_time = time.time()

    main()
    
    elapsed_time = time.time() - start_time

    print('Script executed successfully.')
    print('Duration: ' + str(round(elapsed_time, 2)) + ' Seconds')