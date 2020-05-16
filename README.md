# yahoo_finance_data_scrape
Python application that allows you to pass in a file that has stock tickers on each line and receive an XLSX output for each company that includes Summary, Profile, Income Statement, Balance Sheet, Cash Flow, Valuation Measures, Financial Highlights, and Trading Information data.

The data is scraped from:

[Yahoo Finance Website](https://finance.yahoo.com/)

## Installation

Clone this repository using the "Clone or download" button in the top right corner of the repository or by typing the git clone command:

```bash
git clone https://github.com/tcharts-boop/yahoo_finance_data_scrape.git
```
or for a specific directory:

```bash
git clone https://github.com/tcharts-boop/yahoo_finance_data_scrape.git /specific/directory/
```

After the repository is cloned, navigate to the directory of the cloned repository and install the required dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

To run from the command prompt, you must be in the directory of the cloned repository.

From there you can run by typing:
```bash
python yfinance_scraper.py
```

The script will ask for a text file, you can load any text file with your interested stock tickers.

The format of the text file is so:

```text
ticker_1
ticker_2
ticker_3
ticker_4
and so on...
```

Example:
```text
AAPL
GOOG
NOW
CSCO
VZ
```

Next, the script will ask for a output directory. This is where the script will write each output xlsx file.

## Output

The output workbook for each stock will contain eight sheets: Summary, Profile, Income_Statement, Balance_Sheet, Cash_Flow, Valuation_Measures, Financial_Highlights, and Trading_Information data.


## Author

[Theodore Charts](https://www.linkedin.com/in/tedcharts/)

## License
[MIT](https://choosealicense.com/licenses/mit/)

