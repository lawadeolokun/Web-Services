import pandas as pd
from pymongo import MongoClient

MONGO_URI = "mongodb+srv://admin1:Lawrence2021@cluster0.bqmhjf9.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)

db = client["inventory_db"]
collection = db["products"]

# Load CSV
df = pd.read_csv("data/products.csv")

# Convert to dict
data = df.to_dict(orient="records")

for item in data:
    item["ProductID"] = int(item["ProductID"])
    item["UnitPrice"] = float(item["UnitPrice"])
    item["StockQuantity"] = int(item["StockQuantity"])

# Insert into MongoDB
collection.insert_many(data)

print("Data inserted into MongoDB Atlas!")