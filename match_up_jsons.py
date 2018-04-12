import requests
import json
from bs4 import BeautifulSoup
import codecs
import sys
import sqlite3
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)


### read in jsons


f_pw = open("price_UOwomensdictionary.json","r")
pw_read = f_pw.read()
pw = json.loads(pw_read)
f_pw.close()
#print(pw)

f_pm = open("price_UOmensdictionary.json","r")
pm_read = f_pm.read()
pm = json.loads(pm_read)
f_pm.close()

f_iw = open("UOwomensdictionary.json","r")
iw_read = f_iw.read()
iw = json.loads(iw_read)
f_iw.close()
#print(iw)

f_im = open("UOmensdictionary.json","r")
im_read = f_im.read()
im = json.loads(im_read)
f_im.close()

### check lengths and that all things are there
#for each in pw:
#    print(len(pw[each]))

#print("\n")
#print(len(pw["beauty"]))
#for each in pw["beauty"]:
#    print(each)
#print("\n")

#for each in iw:
#    print(len(iw[each]))

#print("\n")

#for each in pm:
#    print(len(pm[each]))

#print("\n")

#for each in im:
#    print(len(im[each]))

### unsure what the extras are, but just gonna go for it

#n = 0
#while n < 144:
#    print("{} -- {}".format(iw["beauty"][n], pw["beauty"][n]))
#    n = n + 1

### match up with each other

womens = {}
m = 0
categories = ["dresses", "clothing", "jackets", "bottoms", "intimates", "swimwear", "vintage-clothing", "beauty", "accessories", "shoes"]
while m < 10:
    itemlength = len(iw[categories[m]])
    p = 0
    fulllist = []
    while p < itemlength:
        fulllist.append((iw[categories[m]][p], pw[categories[m]][p]))
        p = p + 1
    womens[categories[m]] = fulllist
    m = m + 1

#print(womens)

mens = {}
m = 0
categories = ["graphic-tees", "clothing", "jackets-coats", "bottoms", "shoes", "accessories", "grooming"]
while m < 7:
    itemlength = len(im[categories[m]])
    p = 0
    fulllist = []
    while p < itemlength:
        fulllist.append((im[categories[m]][p], pm[categories[m]][p]))
        p = p + 1
    mens[categories[m]] = fulllist
    m = m + 1

#print(mens)
### make up large dictionary
urbanoutfitters = {"women": womens, "men": mens}

### read into SQL database?
def erase_tables(conn, cur):
    statement = '''
        DROP TABLE IF EXISTS 'Gender';
    '''
    cur.execute(statement)

    statement = '''
        DROP TABLE IF EXISTS 'Items';
    '''
    cur.execute(statement)

    statement = '''
        DROP TABLE IF EXISTS 'Brand';
    '''
    cur.execute(statement)

    statement = '''
        DROP TABLE IF EXISTS 'Category';
    '''
    cur.execute(statement)

    conn.commit()


def make_db(db_name):
    try:
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
    except Error as e:
        print(e)
        return("Failed making database.")

    erase_tables(conn, cur)

    #make each table
    statement = '''
        create TABLE 'Gender' (
            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'Label' TEXT
        );'''

    cur.execute(statement)
    conn.commit()

    statement = '''
        create TABLE 'Items' (
            'BrandId' INTEGER,
            'GenderId' INTEGER,
            'ItemName' TEXT,
            'ListPrice' INTEGER,
            'CategoryId' INTEGER
        );'''

    cur.execute(statement)
    conn.commit()

    statement = '''
        create TABLE 'Brand' (
            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'Name' TEXT
        );'''

    cur.execute(statement)
    conn.commit()

    statement = '''
        create TABLE 'Category' (
            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'Type' TEXT
        );'''

    cur.execute(statement)
    conn.commit()

    conn.close()
    return("Success making database & tables.")

make_db('storeitem.db')

### need to add data to database
### add to "extra" tables first

### Gender table
# just insert "Men" and "Women"
# will autoincrement labels
gend = ["men", "women"]

def insert_gend(gender_list):
    conn = sqlite3.connect("storeitem.db")
    cur = conn.cursor()
    for each in gender_list:
        insertstatement = "insert into Gender "
        insertstatement += "values (NULL, '{}')".format(each)
        cur.execute(insertstatement)
        conn.commit()
    conn.close()

insert_gend(gend)

### Brand table
# insert "AmericanEagle" and "UrbanOutfitters"
# will autoincrement labels
bran = ["AmericanEagle", "UrbanOutfitters"]

def insert_brand(brand_list):
    conn = sqlite3.connect("storeitem.db")
    cur = conn.cursor()
    for each in brand_list:
        insertstatement = "insert into Brand "
        insertstatement += "values (NULL, '{}')".format(each)
        cur.execute(insertstatement)
        conn.commit()
    conn.close()

insert_brand(bran)

### Category table
# insert the keys of the mens & womens dictionaries (no duplicates)
# will autoincrement labels
cats = []
for each in urbanoutfitters: #men women
    for every in urbanoutfitters[each]:
        if every not in cats:
            cats.append(every)
#print(cats)

def insert_cates(cate_list):
    conn = sqlite3.connect("storeitem.db")
    cur = conn.cursor()
    for each in cate_list:
        insertstatement = "insert into Category "
        insertstatement += "values (NULL, '{}')".format(each)
        cur.execute(insertstatement)
        conn.commit()
    conn.close()

insert_cates(cats)

### Item table
# brandid, genderid, categoryid will all be dependent on the other tables
# itemname and listprice will come from dictionary tuples

def insert_items(brand_dictionary):
    conn = sqlite3.connect("storeitem.db")
    cur = conn.cursor()
    for each_gender in brand_dictionary:
        #select code for men
        selectstatement = '''select Id FROM Gender WHERE Label='{}';'''.format(each_gender)
        cur.execute(selectstatement)
        gend_type = cur.fetchone()[0]
        for each_category in brand_dictionary[each_gender]:
            #select code for category
            selectstatement = '''select Id FROM Category WHERE Type='{}';'''.format(each_category)
            cur.execute(selectstatement)
            cate_type = cur.fetchone()[0]
            for each_item in brand_dictionary[each_gender][each_category]:
                #insert statement, have all the information
                insertstatement = '''insert into Items '''
                insertstatement += '''values (2, "{}", "{}", "{}", "{}");'''.format(gend_type, each_item[0], each_item[1], cate_type)
                cur.execute(insertstatement)
                conn.commit()
    conn.close()

insert_items(urbanoutfitters)
