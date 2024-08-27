from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.aave_translation

def get_vocabulary_collection():
    return db.vocabulary
