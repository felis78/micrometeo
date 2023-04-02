from pymongo import MongoClient

client = MongoClient(host="localhost", port=27017)
db_name = "madb"
db = client[db_name]

print(db)


