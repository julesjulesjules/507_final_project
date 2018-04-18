import requests
import json
from bs4 import BeautifulSoup
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)


def UOpricescrape(gender):
    baseurl = "https://www.urbanoutfitters.com/"

    if gender == "mens":
        returndictionary = {}
        categories = ["graphic-tees", "clothing", "jackets-coats", "bottoms", "shoes", "accessories", "grooming"]
        for eachtype in categories:
            pageonerequesturl = baseurl + gender + "-new-" + eachtype
            #make this request, store information
            page_text = requests.get(pageonerequesturl).text
            page_soup = BeautifulSoup(page_text, 'html.parser')
            page_prices = page_soup.find_all(class_ = "c-product-meta__current-price")

            page_one_price_list = []

            for each in page_prices:
                page_one_price_list.append(each.text.strip()[1:])

            #also grab pagination count
            pagelimit = page_soup.find(class_ = "o-pagination__li o-pagination__number--next")
            usepage = int(pagelimit.text)
            start = 2
            #request additional pages and store
            while start <= usepage:
                pageurl = pageonerequesturl + "?page=" + str(start)
                nextpage_text = requests.get(pageurl).text
                nextpage_soup = BeautifulSoup(nextpage_text, 'html.parser')
                other_page_prices = page_soup.find_all(class_ = "c-product-meta__current-price")

                for each in other_page_prices:
                    page_one_price_list.append(each.text.strip()[1:])

                start = start + 1
            returndictionary[eachtype] = page_one_price_list
        return(returndictionary)

    elif gender == "womens":
        #swimwear order switches
        #vintage has no womens
        returndictionary = {}
        categories = ["dresses", "clothing", "jackets", "bottoms", "intimates", "swimwear", "vintage-clothing", "beauty", "accessories", "shoes"]
        for eachtype in categories:
            if eachtype == "vintage-clothing":
                pageonerequesturl = baseurl + "new-" + eachtype
            elif eachtype == "swimwear":
                pageonerequesturl = baseurl + "new-" + gender + '-' + eachtype
            elif eachtype == "dresses":
                pageonerequesturl = baseurl + "new-" + eachtype
            else:
                pageonerequesturl = baseurl + gender + "-new-" + eachtype
            #make this request, store information
            page_text = requests.get(pageonerequesturl).text
            page_soup = BeautifulSoup(page_text, 'html.parser')
            page_prices = page_soup.find_all(class_ = "c-product-meta__current-price")
            #also need to find prices
            page_one_price_list = []

            for each in page_prices:
                page_one_price_list.append(each.text.strip()[1:])

                #also append prices
            #also grab pagination count
            pagelimit = page_soup.find(class_ = "o-pagination__li o-pagination__number--next")
            if pagelimit != None:
                usepage = int(pagelimit.text)
                start = 2
                #request additional pages and store
                while start <= usepage:
                    pageurl = pageonerequesturl + "?page=" + str(start)
                    nextpage_text = requests.get(pageurl).text
                    nextpage_soup = BeautifulSoup(nextpage_text, 'html.parser')
                    other_page_prices = page_soup.find_all(class_ = "c-product-meta__current-price")

                    for each in other_page_prices:
                        page_one_price_list.append(each.text.strip()[1:])
                    start = start + 1
            returndictionary[eachtype] = page_one_price_list

        return(returndictionary)
    else:
        print("gender choice not recongized: {}".format(gender))

#mensUO = UOpricescrape("mens")

#json = json.dumps(mensUO)
#f = open("price_UOmensdictionary.json","w")
#f.write(json)
#f.close()

#womensUO = UOpricescrape("womens")

#json = json.dumps(womensUO)
#f = open("price_UOwomensdictionary.json","w")
#f.write(json)
#f.close()


################################################################################
## Scratch work
################################################################################

#baseurl = "https://www.urbanoutfitters.com/womens-new-arrivals"
#page_text = requests.get(baseurl).text
#page_soup = BeautifulSoup(page_text, 'html.parser')
#items = page_soup.find_all(itemprop = "name")
#pagelimit = page_soup.find(class_ = "o-pagination__li o-pagination__number--next")
#print(pagelimit.text)
# use page limit to determine how many pages to scrape
#usepage = int(pagelimit.text)
#start = 2
#while start != usepage:
#    pageurl = "https://www.urbanoutfitters.com/womens-new-arrivals?page="
#    fullurl = pageurl + str(start)
#    nextpage_text = requests.get(fullurl).text
#    nextpage_soup = BeautifulSoup(nextpage_text, 'html.parser')
#    otheritems = nextpage_soup.find_all(itemprop = "name")
#    start = start + 1

#for each in games:
#    print(each.text)

#anchors = page_soup.find_all('a', class_ = "mobileScoreboardLink")

### WOMENS ###
#page_text = requests.get("https://www.urbanoutfitters.com/mens-new-clothing").text
#page_soup = BeautifulSoup(page_text, 'html.parser')
#page_prices = page_soup.find_all(class_ = "c-product-meta__current-price")
#for each in page_prices:
#    print(each.text.strip()[1:])
