import pandas as pd
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["inventory"]
collection = db["products"]

df = pd.read_csv("data/products.csv")

data = df.to_dict(orient="records")

collection.insert_many(data)

print("Data inserted!")