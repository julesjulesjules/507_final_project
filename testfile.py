import requests
import json
from bs4 import BeautifulSoup
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

baseurl = "https://www.urbanoutfitters.com/womens-new-arrivals"
page_text = requests.get(baseurl).text
page_soup = BeautifulSoup(page_text, 'html.parser')
items = page_soup.find_all(itemprop = "name")
pagelimit = page_soup.find(class_ = "o-pagination__li o-pagination__number--next")
print(pagelimit.text)
# use page limit to determine how many pages to scrape
usepage = int(pagelimit.text)
start = 2
while start != usepage:
    pageurl = "https://www.urbanoutfitters.com/womens-new-arrivals?page="
    fullurl = pageurl + str(start)
    nextpage_text = requests.get(fullurl).text
    nextpage_soup = BeautifulSoup(nextpage_text, 'html.parser')
    otheritems = nextpage_soup.find_all(itemprop = "name")
    start = start + 1

for each in games:
    print(each.text)

#anchors = page_soup.find_all('a', class_ = "mobileScoreboardLink")

### WOMENS ###

def UOwebscrape(gender):
    baseurl = "https://www.urbanoutfitters.com/"
    if gender = "mens":
        categories = ["graphic-tees", "clothing", "jackets-coats", "bottoms", "shoes", "accessories", "grooming"]
        for eachtype in categories:
            pageonerequesturl = baseurl + gender + "-new-" + eachtype
            #make this request, store information
            #also grab pagination count
            #request additional pages and store
    elif gender = "womens":
        #swimwear order switches
        #vintage has no womens
        categories = ["dresses", "clothing", "jackets", "bottoms", "intimates", "swimwear", "vintage-clothing", "beauty", "accessories", "shoes"]
    else:
        print("gender choice not recongized: {}".format(gender))
