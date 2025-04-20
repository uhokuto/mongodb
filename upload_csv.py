
import csv
import urllib.request
import urllib.parse
import urllib
import lxml.html
import time
import pymongo
import pandas as pd
import math


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mognavidb"]
reviews_collection = db['mognavi_reviews']


csv_input = pd.read_csv("../dataset/mognavi9000.csv", encoding='utf8', sep=',',skiprows=0)  

reviews = []
for k, row in csv_input.iterrows():

    rec_dict ={}
    #product_id	p_name	body	misc_dic	_id	rating	reviewer	reviewer_link
    print(row["product_id"])
    rec_dict["product_id"]=int(row["product_id"])
    rec_dict["product_name"]=row["p_name"]
    rec_dict["body"]=row["body"]
    if math.isnan(row["rating"]):
        rec_dict["rating"]=99
    else:
        rec_dict["rating"]=int(row["rating"])
    
    if type(row["reviewer"])==float:
        rec_dict["reviewer"]="none"
        rec_dict["reviewer_link"]="none"
    else:
        rec_dict["reviewer"]=row["reviewer"]
        rec_dict["reviewer_link"]=row["reviewer_link"]
        
    reviews.append(rec_dict)

    
reviews_collection.insert_many(reviews)