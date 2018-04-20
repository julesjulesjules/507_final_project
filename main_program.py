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
from class_def import *

################################################################################

def load_help_text():
    with open('help.txt') as f:
        return f.read()

################################################################################
print("\n")
print("***********************************************************************")
print("                          Before We Begin                              ")
print("***********************************************************************")
print("\n")
print("rebuild: re-scrapes websites & builds a new database from updated data ")
print("current: re-builds the database from current files                     ")
print("none: moves on to use the database that currently exists               ")
print("\n")

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
print("\n")
print("***********************************************************************")
print("                    New Arrivals Clothing Search                       ")
print("***********************************************************************")
print("\n")
print("***********************************************************************")
print("          For instructions, type help, otherwise type next             ")
print("\n")
user_instruct_or_no = input(">>>  ")

check2 = 0
while check2 != 1:
    if user_instruct_or_no == "help":
        help_text = load_help_text()
        print(help_text)
        ### print instructions
        print("\n")
        print("***********************************************************************")
        print("\n")
        check2 = 1
    elif user_instruct_or_no == "next":
        check2 = 1
    else:
        print("unrecognized command: {}".format(user_action))
        #### probably should also make this a while loop
        user_instruct_or_no = input(">>>  ")

print("\n")
user_ask = input("Would you like to save your searches today? yes/no ")
if user_ask == "yes":
    user_cred_name = input("Type your name and press enter: ")
    user_cred_password = input("Type a password and press enter: ")
    current_user = Remember(user_cred_name, user_cred_password)
    ### search
    user_search_action = 0
    while user_search_action != "exit":
        user_search_action = input("What search method would you like, pattern/price/compare/exit: ")
        if user_search_action == "pattern":
            patt_r = find_a_pattern()
            current_user.collection(patt_r)
        elif user_search_action == "price":
            price_r = find_high_low_price()
            current_user.collection(price_r)
        elif user_search_action == "compare":
            comp_r = compare_men_women()
            current_user.collection(comp_r)
        elif user_search_action == "exit":
            print("Goodbye!")
        else:
            print("unrecognized command: {}".format(user_search_action))
else: 
    ### search
    user_search_action = 0
    while user_search_action != "exit":
        user_search_action = input("What search method would you like, pattern/price/compare/exit: ")
        if user_search_action == "pattern":
            find_a_pattern()
        elif user_search_action == "price":
            find_high_low_price()
        elif user_search_action == "compare":
            compare_men_women()
        elif user_search_action == "exit":
            print("Goodbye!")
        else:
            print("unrecognized command: {}".format(user_search_action))
