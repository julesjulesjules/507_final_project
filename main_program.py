################################################################################
# external

import requests
import json
from bs4 import BeautifulSoup
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

################################################################################
# internal

from testfile import *
from match_up_jsons import *
from anthroscrape import *
from anthro_json import *
from working_clothes_functions import *

################################################################################

user_action = input("What would you like to do?")

if user_action == "rebuild":
# if i want to rebuild the database completely:

    #need to re-scrape Urban Outfitters

    # run UOpricescrape(gender) from testfile.py
    # can probably create a function for writing the files???
    mensUO = UOpricescrape("mens")
    json_muo = json.dumps(mensUO)
    f_muo = open("price_UOmensdictionary.json","w")
    f_muo.write(json_muo)
    f_muo.close()

    womensUO = UOpricescrape("womens")
    json_wuo = json.dumps(womensUO)
    f_wuo = open("price_UOwomensdictionary.json","w")
    f_wuo.write(json_wuo)
    f_wuo.close()

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


    # need to rescrape anthropologie:
    ascrape = anthroScrape()
    json_ant = json.dumps(ascrape)
    f_ant = open("anthropologie_scrape.json","w")
    f_ant.write(json_ant)
    f_ant.close()

### then continue
elif user_action == "current":
# if i want to rebuild the database from current files:
    # just need to read in files:
    uofiles = read_in_UOfiles()
    womens = matchUOwomens(uofiles[0], uofiles[1])
    mens = matchUOmens(uofiles[2], uofiles[3])

    antfile = read_in_ANTfiles()
    anthro_w = match_anthros(antfile)

    urbanoutfitters = {"women": womens, "men": mens}
    #set up db
    make_db('storeitem.db')
    #load in all accessory tables

    gend = ["men", "women"]
    insert_gend(gend)

    bran = ["Anthropologie", "UrbanOutfitters"]
    insert_brand(bran)

    cats = []
    for each in urbanoutfitters: #men women
        for every in urbanoutfitters[each]:
            if every not in cats:
                cats.append(every)
    for each in anthro_w:
        if each not in cats:
            cats.append(each)
    insert_cates(cats)

    insert_items(urbanoutfitters)
    insert_items_ant(anthro_w)

else:
    print("unrecognized command: {}".format(user_action))

## then just use database

#elif user_action == "database":
    # if i want to use the current database
#    pass
