import csv
import requests
from BeautifulSoup import BeautifulSoup

"""
To run in Python shell:
>>> from scrape import scrape_regent
>>> scrape_regent()
"""
def scrape_regent():
    menu_items = []
    url = 'http://www.regentthai.com/menu.html'
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html)
    for ul in soup.findAll('ul', {'class': 'menu'}):
        for item in ul.findAll('li'):
            if item.div:
                name = item.text.replace(item.div.text, '').encode('utf-8')
                desc = item.div.text.split('$')[0].encode('utf-8')
            else:
                name = item.text.replace(item.span.text, '').encode('utf-8')
                desc = None
            if item.span:
                price = item.span.text.encode('utf-8')
            else:
                price = None
            menu_items.append(['Regent Thai', name, desc, price ])

    outfile = open("regent_thai.csv", "wb")
    writer = csv.writer(outfile)
    writer.writerow(["Restaurant", "Item", "Description", "Price"])
    writer.writerows(menu_items)
