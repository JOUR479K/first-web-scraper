import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'https://columbian.gwu.edu/2015-2016'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table')

list_of_rows = []
counter = 1
for row in table.findAll('tr')[1:-1]:
    list_of_cells = []
    for cell in row.findAll('td'):
        if cell.find('href'):
            list_of_cells.append("https://columbian.gwu.edu/2015-2016" + cell.find('href')['href'])
        else:
            list_of_cells.append(cell.text)
    list_of_rows.append(list_of_cells)

outfile = open("grants1.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Department", "Faculty", "Sponsor", "Title"])
writer.writerows(list_of_rows)
