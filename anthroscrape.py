import requests
import json
from bs4 import BeautifulSoup
import codecs
import sys
#sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

def anthroScrape():
    baseurl = "https://www.anthropologie.com/new-"
    returndictionary = {}
    categories = ["dresses", "tops", "sweaters", "jackets-coats", "jeans", "pants", "shorts", "skirts", "jumpsuits-rompers", "swimwear", "intimates-sleepwear", "loungewear", "activewear", "petite-clothing"]
    for eachtype in categories:
        pagerequesturl = baseurl + eachtype
        page_text = requests.get(pagerequesturl).text
        page_soup = BeautifulSoup(page_text, 'html.parser')
        page_items = page_soup.find_all(class_ = "c-product-tile__h3 c-product-tile__h3--regular")
        #print(len(page_items))
        page_prices = page_soup.find_all(class_ = "c-product-meta__current-price")
        #print(len(page_prices))

        if len(page_items) == len(page_prices):
            cat_item_list = []
            cat_price_list = []
            for each in page_items:
                cat_item_list.append([each.text.strip()])
            for each in page_prices:
                cat_price_list.append(each.text.strip()[1:])

        pagelimit = page_soup.find(class_ = "o-pagination__li o-pagination__number--next")
        if pagelimit != None:
            usepage = int(pagelimit.text)
            start = 2
            #request additional pages and store
            while start <= usepage:
                pageurl = pagerequesturl + "?page=" + str(start)
                nextpage_text = requests.get(pageurl).text
                nextpage_soup = BeautifulSoup(nextpage_text, 'html.parser')
                other_page_items = page_soup.find_all(class_ = "c-product-tile__h3 c-product-tile__h3--regular")
                other_page_prices = page_soup.find_all(class_ = "c-product-meta__current-price")

                for each in other_page_items:
                    cat_item_list.append([each.text.strip()])
                for each in other_page_prices:
                    cat_price_list.append(each.text.strip()[1:])
                start = start + 1

        returndictionary[eachtype] = [cat_item_list, cat_price_list]
    return(returndictionary)

#ascrape = anthroScrape()

#json = json.dumps(ascrape)
#f = open("anthropologie_scrape.json","w")
#f.write(json)
#f.close()


#<h3 class="c-product-tile__h3 c-product-tile__h3--regular" data-qa-prod-title="">
#        <span>
#            Barcelona Dress
#        </span>
#    </h3>

#    <span class="c-product-meta__current-price" data-qa-current-price="">
#                        $198.00</span>

#<li data-qa-total-pages="" class="o-pagination__li o-pagination__number--next">

#                    10

#                </li>
