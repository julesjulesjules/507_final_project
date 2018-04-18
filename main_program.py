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

from testfile.py import *
from match_up_jsons.py import *

################################################################################

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

    # need to rescrape anthropologie:



# if i want to rebuild the database from current files:
    # just need to read in files:
    uofiles = read_in_UOfiles()
    womens = matchUOwomens(uofiles[0], uofiles[1])
    mens = matchUOmens(uofiles[2], uofiles[3])



# if i want to use the current database
