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

################################################################################

# if i want to rescrape urban outfitters then:
    # run UOpricescrape(gender) from testfile.py
    # can probably create a function for writing the files???
    mensUO = UOpricescrape("mens")
    json = json.dumps(mensUO)
    f = open("price_UOmensdictionary.json","w")
    f.write(json)
    f.close()

    womensUO = UOpricescrape("womens")
    json = json.dumps(womensUO)
    f = open("price_UOwomensdictionary.json","w")
    f.write(json)
    f.close()

# if i want to rescrape anthropologie:

# if i want to rebuild the database:
