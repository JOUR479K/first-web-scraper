import csv
import requests
from BeautifulSoup import BeautifulSoup

years = ['2010-2011', '2011-2012', '2012-2013', '2013-2014', '2014-2015', '2015-2016']
list_of_rows = []

for year in years:
    print year
    response = requests.get('https://columbian.gwu.edu/' + year)
    html = response.content
    soup = BeautifulSoup(html)
    table = soup.find('table')
    for row in table.findAll('tr')[1:]:
        list_of_cells = []
        list_of_cells.append(year)
        for cell in row.findAll('td'):
            list_of_cells.append(cell.text.encode('utf-8'))
        list_of_rows.append(list_of_cells)

outfile = open("grants.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Year", "Department", "Faculty", "Sponsor", "Title"])
writer.writerows(list_of_rows)
