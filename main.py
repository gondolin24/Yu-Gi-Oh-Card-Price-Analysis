import csv
import numpy
import urllib.request
from bs4 import BeautifulSoup

web_url = "https://yugiohprices.com/browse_sets?set=Cybernetic+Horizon"


page = urllib.request.urlopen(web_url)
soup = BeautifulSoup(page, 'html.parser')

listOfCards = soup.findAll('tr', attrs={'class': 'content'})

cardMatrix = numpy.matrix(["Card Name", "Lowest Price", "Average Price", "Highest Price"])
cardNameSet = {"Card Name"}


f = open('CyberneticHorizon.csv', 'w')

for card in listOfCards:
# filter out all ebay links
    if "eBay" not in card.text:
        f.write(card.contents[3].text.replace("\n", ""))
        f.write("|")
        f.write(card.contents[11].text.replace("\n", ""))
        f.write("|")
        f.write(card.contents[13].text.replace("\n", ""))
        f.write("|")
        f.write(card.contents[15].text.replace("\n", ""))
        f.write("\n")
       # cardNameSet.add(card.contents[3].text.replace("\n", ""))

f.close()

print(cardNameSet)
