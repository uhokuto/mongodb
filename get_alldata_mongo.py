
import csv
import urllib.request
import urllib.parse
import urllib
import lxml.html
import time
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["shareviewdb"]
reviews_collection = db['shareview_reviews']


count=0
for data in reviews_collection.find(no_cursor_timeout=True):
    pprint.pprint(data)
    count+=1
    print(count)
    #if count >=10:
    #    input()
    #newvalues = { "$set": { "pref": "京都" } }
    #reviews_collection.update_one(data, newvalues)
 
    
    