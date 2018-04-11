import requests
import json
from bs4 import BeautifulSoup
import codecs
import sys
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
for each in pw:
    print(len(pw[each]))

print("\n")
print(len(pw["beauty"]))
for each in pw["beauty"]:
    print(each)
print("\n")

for each in iw:
    print(len(iw[each]))

print("\n")

for each in pm:
    print(len(pm[each]))

print("\n")

for each in im:
    print(len(im[each]))

### unsure what the extras are, but just gonna go for it

n = 0
while n < 144:
    print("{} -- {}".format(iw["beauty"][n], pw["beauty"][n]))
    n = n + 1

### match up with each other
### make up large dictionary
### read into SQL database?
