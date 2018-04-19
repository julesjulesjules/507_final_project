#### working with database

#import requests
#import json
#from bs4 import BeautifulSoup
import codecs
import sys
import sqlite3
#sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
import plotly.plotly as py
import plotly.graph_objs as go

### find a pattern:
def find_a_pattern():
    try:
        conn = sqlite3.connect("storeitem.db")
        cur = conn.cursor()
    except Error as e:
        print(e)
        print("Failed to connect to database.")

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

    cur.execute(statement)
    print("\n")
    print("*******************************************************************")
    print("\n")
    for each in cur:
        print("{:<15} {:<30} {:<8}".format(each[0], each[1][:30], each[2]))
    print("\n")
    print("*******************************************************************")
    print("\n")
    conn.close()
    #return()

#find_a_pattern()

def find_high_low_price():
    try:
        conn = sqlite3.connect("storeitem.db")
        cur = conn.cursor()
    except Error as e:
        print(e)
        print("Failed to connect to database.")

    ### need a list of items to look for?
    il_statement = '''select Type from Category'''
    cur.execute(il_statement)
    itemlist = []
    for each in cur:
        itemlist.append(each[0])
    ## print out this so user knows choices
    print("*******************************************************************")
    start = 0
    a = 0
    b = 6
    c = 12
    d = 18
    #24 categories
    while start < 6:
        print("{:<19}  {:<19}  {:<19}  {:<19}".format(itemlist[a], itemlist[b], itemlist[c], itemlist[d]))
        start = start + 1
        a = a + 1
        b = b + 1
        c = c + 1
        d = d + 1
    print("*******************************************************************")
    print("\n")
    cat_choice = input("What type of items are you looking for? ")
    gend_choice = input("Choose mens/womens/both: ")
    how_many = input("How many items would you like to look at? #/all ")
    top_bottom = input("Are you looking for most/least expensive? ")

    cat_statement = '''select Id FROM Category WHERE Type="{}"'''.format(cat_choice)
    ### grab the number, use it below
    cur.execute(cat_statement)
    cat_num = cur.fetchone()[0]
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

    if top_bottom == "most":
        statement += '''ORDER BY ListPrice DESC '''
    if top_bottom == "least":
        statement += '''ORDER BY ListPrice ASC '''

    if how_many != "all":
        statement += '''LIMIT {} '''.format(how_many)

    cur.execute(statement)
    print("\n")
    print("*******************************************************************")
    print("\n")
    for each in cur:
        print("{:<15} {:<30} {:<8}".format(each[0], each[1][:30], each[2]))
    print("\n")
    print("*******************************************************************")
    print("\n")
    conn.close()
    #return()

#find_high_low_price()

def compare_men_women():
    try:
        conn = sqlite3.connect("storeitem.db")
        cur = conn.cursor()
    except Error as e:
        print(e)
        print("Failed to connect to database.")

    user_c = input("Choose max/average: ")
    if user_c == "max":
        agg = "MAX"
    if user_c == "average":
        agg = "AVG"
    #select category names, average price
    #men
    statement = '''select Type, round({}(ListPrice), 2) '''.format(agg)
    statement += '''FROM Items JOIN Category ON Items.CategoryId=Category.Id '''
    statement += '''GROUP BY Type '''
    statement += '''HAVING GenderId=1;'''
    cur.execute(statement)
    men_d = {}
    for each in cur:
        men_d["men " + each[0]] = each[1]

    #women
    statement = '''select Type, round({}(ListPrice), 2) '''.format(agg)
    statement += '''FROM Items JOIN Category ON Items.CategoryId=Category.Id '''
    statement += '''GROUP BY Type '''
    statement += '''HAVING GenderId=2;'''
    cur.execute(statement)
    women_d = {}
    for each in cur:
        women_d["women " + each[0]] = each[1]
    conn.close
    # do it for men and women
    #put it into list for plotly
    x = []
    y = []
    for each in women_d:
        x.append(each)
        y.append(women_d[each])
    for every in men_d:
        x.append(every)
        y.append(men_d[every])
    # use plotly to graph it all

    data = [go.Bar(
                x=x,
                y=y,
                text=y,
                textposition = 'auto',
                marker=dict(
                    color='rgb(158,202,225)',
                    line=dict(
                        color='rgb(8,48,107)',
                        width=1.5),
                ),
                opacity=0.6
            )]

    py.plot(data, filename='bar-direct-labels')

#compare_men_women()
