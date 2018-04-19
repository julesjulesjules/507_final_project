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
    print("Failed to connect to database.")

### find a pattern:
def find_a_pattern():
    pat_choice = input("What pattern are you looking for? stripe/dot/floral/plaid ")
    gend_choice = input("Choose mens/womens/both: ")
    how_many = input("How many items would you like to look at? #/all ")

    statement = '''select Brand.Name, ItemName, ListPrice '''
    statement += '''FROM Items JOIN Brand ON Brand.Id=Items.BrandId '''
    ### gender
    if gend_choice == "mens":
        statement += '''WHERE Items.GenderId=1 '''
        statement += '''AND ItemName LIKE '%{}%' '''.format(pat_choice)
    if gend_choice == "womens":
        statement += '''WHERE Items.GenderId=2 '''
        statement += '''AND ItemName LIKE '%{}%' '''.format(pat_choice)
    if gend_choice == "both":
        statement += '''WHERE ItemName LIKE '%{}%' '''.format(pat_choice)

    if how_many != "all":
        statement += '''LIMIT {}'''.format(how_many)

    return(statement)

print(find_a_pattern())
conn.close()
