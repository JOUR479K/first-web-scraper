import csv
import requests
from BeautifulSoup import BeautifulSoup

years = ['2015-2016', '2013-14', '2011-2012']
for year in years:
    url = 'https://columbian.gwu.edu/' + year
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html)
    table = soup.find('table')

    list_of_rows = []
    for row in table.findAll('tr'):
        list_of_cells = []
        list_of_cells.append(year)
        for cell in row.findAll('td'):
    		list_of_cells.append(cell.text)
    	list_of_rows.append(list_of_cells)

outfile = open("grants.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Year", "Department", "Faculty", "Sponsor", "Title",])
writer.writerows(list_of_rows)
