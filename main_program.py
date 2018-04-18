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

# if i want to rescrape anthropologie:

# if i want to rebuild the database:
