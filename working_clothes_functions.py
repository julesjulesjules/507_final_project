import requests
import json
from bs4 import BeautifulSoup
import codecs
import sys
#sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)


def UOwebscrape(gender):
    baseurl = "https://www.urbanoutfitters.com/"

    if gender == "mens":
        returndictionary = {}
        categories = ["graphic-tees", "clothing", "jackets-coats", "bottoms", "shoes", "accessories", "grooming"]
        for eachtype in categories:
            pageonerequesturl = baseurl + gender + "-new-" + eachtype
            #make this request, store information
            page_text = requests.get(pageonerequesturl).text
            page_soup = BeautifulSoup(page_text, 'html.parser')
            page_items = page_soup.find_all(class_ = "c-product-tile__h3 c-product-tile__h3--regular")

            #also need to find prices
            page_one_item_list = []
            n = 0
            for each in page_items:
                if n < 18:
                    pass
                else:
                    page_one_item_list.append(each.text.strip())
                n = n + 1
                #also append prices
            #also grab pagination count
            pagelimit = page_soup.find(class_ = "o-pagination__li o-pagination__number--next")
            usepage = int(pagelimit.text)
            start = 2
            #request additional pages and store
            while start <= usepage:
                pageurl = pageonerequesturl + "?page=" + str(start)
                nextpage_text = requests.get(pageurl).text
                nextpage_soup = BeautifulSoup(nextpage_text, 'html.parser')
                otheritems = nextpage_soup.find_all(class_ = "c-product-tile__h3 c-product-tile__h3--regular")
                n = 0
                for each in otheritems:
                    if n < 18:
                        pass
                    else:
                        page_one_item_list.append(each.text.strip())
                    n = n + 1

                    #also append prices as tuples??? so list of tuples?
                start = start + 1
            returndictionary[eachtype] = page_one_item_list
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
            page_items = page_soup.find_all(class_ = "c-product-tile__h3 c-product-tile__h3--regular")
            #also need to find prices
            page_one_item_list = []
            n = 0
            for each in page_items:
                if n < 21:
                    pass
                else:
                    page_one_item_list.append(each.text.strip())
                n = n + 1
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
                    otheritems = nextpage_soup.find_all(class_ = "c-product-tile__h3 c-product-tile__h3--regular")
                    n = 0
                    for each in otheritems:
                        if n < 21:
                            pass
                        else:
                            page_one_item_list.append(each.text.strip())
                        n = n + 1

                        #also append prices as tuples??? so list of tuples?
                    start = start + 1
            returndictionary[eachtype] = page_one_item_list

        return(returndictionary)
    else:
        print("gender choice not recongized: {}".format(gender))


mensUOitems = UOwebscrape("mens")

json_muoi = json.dumps(mensUOitems)
f_muoi = open("UOmensdictionary.json","w")
f_muoi.write(json_muoi)
f_muoi.close()

womensUOitems = UOwebscrape("womens")

json_wuoi = json.dumps(womensUOitems)
f_wuoi = open("UOwomensdictionary.json","w")
f_wuoi.write(json_wuoi)
f_wuoi.close()

#mensUO = UOwebscrape("mens")

#json = json.dumps(mensUO)
#f = open("UOmensdictionary.json","w")
#f.write(json)
#f.close()

#womensUO = UOwebscrape("womens")

#json = json.dumps(womensUO)
#f = open("UOwomensdictionary.json","w")
#f.write(json)
#f.close()
