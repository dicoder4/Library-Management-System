from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["library_db"]
users_collection = db["users"]
