import csv
import numpy
import urllib.request
from bs4 import BeautifulSoup

web_url = "https://yugiohprices.com/browse_sets?set=Cybernetic+Horizon"


page = urllib.request.urlopen(web_url)
soup = BeautifulSoup(page, 'html.parser')

listOfCards = soup.findAll('tr', attrs={'class': 'content'})

cardMatrix = numpy.matrix(["Card Name", "Lowest Price", "Average Price", "Highest Price"])

for card in listOfCards:
# filter out all ebay links
    if "ebay" not in card.text:
        print(card.text)


print("hello world")
