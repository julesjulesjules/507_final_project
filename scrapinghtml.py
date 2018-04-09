import requests
import json
from bs4 import BeautifulSoup

#just to request the html
#store it, will sort through it all later

daystoscrape = [313, 314, 315, 316, 317, 318, 322, 323, 324, 325, 331, 402]
baseurl = "http://www.espn.com/mens-college-basketball/scoreboard/_/date/20180"

### on each of these pages, need to grab each game unit

def grab_game_units(page_date):
    #baseurl for start page (from calendar)
    baseurl = "http://www.espn.com/mens-college-basketball/scoreboard/_/date/20180"
    full_url = baseurl + str(page_date)
    page_text = requests.get(full_url).text
    #page_soup = BeautifulSoup(page_text, 'html.parser')
    return page_text

#writeoutfirsthtml = {}
#for each_number in daystoscrape:
#    writeoutfirsthtml[each_number] = grab_game_units(each_number)

## write out to text file:
#with open("roundone_scrape.txt", "w") as ftowrite:
#    ftowrite.write(json.dumps(writeoutfirsthtml))
