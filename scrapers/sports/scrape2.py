import csv
import requests
from BeautifulSoup import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')


response = requests.get("http://m.nationals.mlb.com/roster/transactions/2017/03")
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table')

list_of_rows = []
for row in table.findAll('tr')[1:]:
    list_of_cells = []

    for cell in row.findAll('td'):
  		if cell.find('a'):
       		 list_of_cells.append(cell.find('a')['href'])
    else:
        list_of_cells.append(cell.text)
        list_of_cells.append(cell.text.encode('utf-8'))
    list_of_rows.append(list_of_cells)




outfile = open("transactions.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Date","URL", "Text"])
writer.writerows(list_of_rows)
