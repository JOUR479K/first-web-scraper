import csv
import requests
from BeautifulSoup import BeautifulSoup

url = "http://m.mlb.com/was/roster/transactions/2017/"
list_of_rows = []
months = ['04', '03', '02', '01']

for month in months:
    response = requests.get(url+month)
    html = response.content
    soup = BeautifulSoup(html)
    table = soup.find('table')

    for row in table.findAll('tr')[1:]:
        list_of_cells = []
        for cell in row.findAll('td'):
            if cell.find('a'):
                link = cell.find('a')['href']
                list_of_cells.append(link)
                list_of_cells.append(cell.text)
            else:
                list_of_cells.append(cell.text)
        list_of_rows.append(list_of_cells)


outfile = open("transactions.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["date", "url", "text"])
writer.writerows(list_of_rows)
