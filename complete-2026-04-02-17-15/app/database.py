from pymongo import MongoClient

MONGO_URI = "mongodb+srv://admin1:Lawrence2021@cluster0.bqmhjf9.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)

db = client["inventory_db"]
collection = db["products"]