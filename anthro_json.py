#anthroJSONs
import requests
import json
from bs4 import BeautifulSoup
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

def read_in_ANTfiles():
    ant = open("anthropologie_scrape.json","r")
    ant_read = ant.read()
    anthro = json.loads(ant_read)
    ant.close()
    return(anthro)

def match_anthros(anthro):
    matched_dictionary = {}
    for each in anthro:
        print(each) # categories
        print(type(anthro[each])) # 2 (one for items, one for prices) #list
        len_len = len(anthro[each][0])
        n = 0
        cat_list = []
        while n < len_len:
            insert_tup = (anthro[each][0][n], anthro[each][1][n])
            cat_list.append(insert_tup)
            n = n + 1
        matched_dictionary[each] = cat_list
    return(matched_dictionary)

#for each in matched_dictionary:
    #print(each)
    #print(len(matched_dictionary[each]))





#for every_item in anthro[each][0]): #list
    #match with each_price in anthro[each][1]
