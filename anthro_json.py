#anthroJSONs
import requests
import json
from bs4 import BeautifulSoup
import codecs
import sys
import sqlite3
#sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

def read_in_ANTfiles():
    ant = open("anthropologie_scrape.json","r")
    ant_read = ant.read()
    anthro = json.loads(ant_read)
    ant.close()
    return(anthro)

def match_anthros(anthro):
    matched_dictionary = {}
    for each in anthro:
        #print(each) # categories
        #print(type(anthro[each])) # 2 (one for items, one for prices) #list
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


aant = read_in_ANTfiles()
for each in aant:
    print(each)
    print(len(aant[each][0]))
    print(len(aant[each][1]))

print(aant["petite-clothing"])
aant_two = match_anthros(aant)
#for each in aant_two:
#    print(each)
#    print(len(aant_two[each]))
#    for every_tuple in aant_two[each]:
#        print(every_tuple)

#for every_item in anthro[each][0]): #list
    #match with each_price in anthro[each][1]



def insert_items_ant(brand_dictionary):
    conn = sqlite3.connect("storeitem.db")
    cur = conn.cursor()
    for each_category in brand_dictionary:
        #select code for category
        selectstatement = '''select Id FROM Category WHERE Type='{}';'''.format(each_category)
        cur.execute(selectstatement)
        cate_type = cur.fetchone()[0]
        for each_item in brand_dictionary[each_category]:
            #insert statement, have all the information
            insertstatement = '''insert into Items '''
            insertstatement += '''values (1, 2, "{}", "{}", "{}");'''.format(each_item[0][0], each_item[1], cate_type)
            cur.execute(insertstatement)
            conn.commit()
    conn.close()
