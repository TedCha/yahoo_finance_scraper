from bs4 import BeautifulSoup
import pandas as pd

html_doc = 'companies.html'

soup = BeautifulSoup(open(html_doc, encoding='utf8'), 'lxml')

headers = soup.select('.col-xs-9')

company_list = []

for i in range(len(headers)):
    company = (headers[i].contents[0]).strip()

    company_list.append(company)

with open('companies.txt', 'w', encoding='utf8') as file:
    file.write("\n".join(company_list))
    file.close()
