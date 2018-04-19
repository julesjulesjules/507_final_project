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
from second_level import *
from working_with_database import *

################################################################################

user_action = input("What would you like to do (rebuild/current/none)? ")
check = 0
while check != 1:
    if user_action == "rebuild":
    # if i want to rebuild & rescrape
        rescrape_and_rebuild()
        check = 1
    ### then continue
    elif user_action == "current":
    # if i want to rebuild the database from current files:
        just_rebuild()
        check = 1
    elif user_action == "none":
        print("Excellent, moving on then.")
        check = 1
    else:
        print("unrecognized command: {}".format(user_action))
        user_action = input("What would you like to do (rebuild/current/none)? ")

## then just use database
print("***********************************************************************")
print("                          Clothing Search                              ")
print("***********************************************************************")
print("\n")
print("***********************************************************************")
print("          For instructions, type help, otherwise type next             ")
user_instruct_or_no = input(">>>  ")
if user_instruct_or_no == "help":
    pass
    ### print instructions
    #print("***********************************************************************")
elif user_instruct_or_no == "next":
    pass
else:
    print("unrecognized command: {}".format(user_action))
    #### probably should also make this a while loop

### search
user_search_action = 0
while user_search_action != "exit":
    user_search_action = input("What search method would you like, pattern/price: ")
    if user_search_action == "pattern":
        find_a_pattern()
    elif user_search_action == "price":
        find_high_low_price()
    elif user_search_action == "exit":
        print("Goodbye!")
    else:
        print("unrecognized command: {}".format(user_search_action))
