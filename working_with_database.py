#### working with database

#import requests
#import json
#from bs4 import BeautifulSoup
import codecs
import sys
import sqlite3
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

try:
    conn = sqlite3.connect("storeitem.db")
    cur = conn.cursor()
except Error as e:
    print(e)
    return("Failed to connect to database.")

### find a pattern:
def find_a_pattern():
    pat_choice = input("What pattern are you looking for? stripe/dot/floral/plaid ")
    gend_choice = input("Choose mens/womens/both: ")
    how_many = input("How many items would you like to look at? #/all ")
    
