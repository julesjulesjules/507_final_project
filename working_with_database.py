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

#print(find_a_pattern())

def find_high_low_price():
    ### need a list of items to look for?
    cat_choice = input("What type of items are you looking for? ")
    gend_choice = input("Choose mens/womens/both: ")
    how_many = input("How many items would you like to look at? #/all ")
    top_bottom = input("Are you looking for most/least expensive? ")

    cat_statement = '''select CategoryId FROM Category WHERE Type="{}"'''.format(cat_choice)
    ### grab the number, use it below
    ## save in cat_num

    statement = '''select Brand.Name, ItemName, ListPrice '''
    statement += '''FROM Items JOIN Brand ON Brand.Id=Items.BrandId '''

    if gend_choice == "mens":
        statement += '''WHERE Items.GenderId=1 '''
        statement += '''AND Items.CategoryId={} '''.format(cat_num)
    if gend_choice == "womens":
        statement += '''WHERE Items.GenderId=2 '''
        statement += '''AND Items.CategoryId={} '''.format(cat_num)
    if gend_choice == "both":
        statement += '''WHERE Items.CategoryId={} '''.format(cat_num)

    if how_many != "all":
        statement += '''LIMIT {}'''.format(how_many)

    if top_bottom == "most":
        statement += '''DESC '''
    if top_bottom == "least":
        statement += '''ASC '''





conn.close()
