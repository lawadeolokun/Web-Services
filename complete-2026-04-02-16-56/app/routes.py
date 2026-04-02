from fastapi import APIRouter
from app.database import collection
from app.models import Product
import requests

router = APIRouter()

# GET SINGLE
@router.get("/getSingleProduct/{id}")
def get_product(id: int):
    return collection.find_one({"ProductID": id}, {"_id": 0})

# GET ALL
@router.get("/getAll")
def get_all():
    return list(collection.find({}, {"_id": 0}))

# ADD NEW
@router.post("/addNew")
def add_product(product: Product):
    collection.insert_one(product.dict())
    return {"message": "Added"}

# DELETE
@router.delete("/deleteOne/{id}")
def delete_product(id: int):
    collection.delete_one({"ProductID": id})
    return {"message": "Deleted"}

# STARTS WITH
@router.get("/startsWith/{letter}")
def starts_with(letter: str):
    return list(collection.find(
        {"Name": {"$regex": f"^{letter}", "$options": "i"}},
        {"_id": 0}
    ))

# PAGINATION
@router.get("/paginate")
def paginate(start: int, end: int):
    return list(collection.find(
        {"ProductID": {"$gte": start, "$lte": end}},
        {"_id": 0}
    ).limit(10))

# CONVERT USD → EUR
@router.get("/convert/{id}")
def convert_price(id: int):
    product = collection.find_one({"ProductID": id})

    rate = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    euro = rate["rates"]["EUR"]

    return {
        "Name": product["Name"],
        "Price_EUR": round(product["UnitPrice"] * euro, 2)
    }