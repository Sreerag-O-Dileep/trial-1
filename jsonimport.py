import json
import pymongo
import pandas as pd
myclient = pymongo.MongoClient()

df = pd.read_csv('x.csv')   # loading csv file
df.to_json('y.json')        # saving to json file
jdf = open('y.json').read() # loading the json file 
data = json.loads(jdf)             
print(data)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["config"]
collection = db["test"]
db.collection.insert_one(data)
db.collection.create_index([('id', pymongo.ASCENDING)], unique=True)