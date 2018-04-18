import requests
import json
from bs4 import BeautifulSoup
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

#just to request the html
#store it, will sort through it all later

daystoscrape = [313, 314, 315, 316, 317, 318, 322, 323, 324, 325, 331, 402]
baseurl = "http://www.espn.com/mens-college-basketball/scoreboard/_/date/20180"

### on each of these pages, need to grab each game unit

def grab_game_units(page_date):
    #baseurl for start page (from calendar)
    baseurl = "http://www.espn.com/mens-college-basketball/scoreboard/_/group/100/date/20180"
    full_url = baseurl + str(page_date)
    page_text = requests.get(full_url).text
    page_soup = BeautifulSoup(page_text, 'lxml')
    anchors = page_soup.find_all('a', class_ = "mobileScoreboardLink")
    print(len(anchors))
    return page_text

writeoutfirsthtml = {}
for each_number in daystoscrape:
    writeoutfirsthtml[each_number] = grab_game_units(each_number)


## write out to text file:
#with open("roundone_scrape.txt", "w") as ftowrite:
#    ftowrite.write(json.dumps(writeoutfirsthtml))

#with open("roundone_scrape.txt", "r") as f:
#    r = f.read()
#    n = json.loads(r)

#linklist = []
#print(type(n))
#for each in n:
#    soup = BeautifulSoup(n[each], 'html.parser')
#    emailitems = soup.find_all(class_ = "mobileScoreboardLink")

#    for each in emailitems:
#        emaillink = each.find_all(a['href'])
#        linklist.append(emaillink)
#print(linklist)

#page_soup = BeautifulSoup(page_text, 'html.parser')
#emailitems = page_soup.find_all('a', class_ = "mobileScoreboardLink")
#nextlinklist = []
#for each in emailitems:
#    nextlinklist.append(emailitems.find('a')['href'])
