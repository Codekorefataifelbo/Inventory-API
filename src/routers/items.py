from fastapi import APIRouter, HTTPException, Depends, File, UploadFile
from starlette.responses import FileResponse
from typing import Optional

from utilities import find_item
from authentication import authenticate
from schema import Item, ItemUpdate  # Importing the schemas
from models import DBItem, SessionLocal  # Importing the database model
import os

router = APIRouter()

@router.post("/items")
def create_item(item: Item, authenticated: bool = Depends(authenticate)):
    db = SessionLocal()
    new_item = DBItem(name=item.name, quantity=item.quantity)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return {"item": new_item}

@router.get("/items")
async def get_items():
    db = SessionLocal()
    items = db.query(DBItem).all()
    return {"items": items}

@router.get("/items/{item_id}")
def get_item(item_id: int):
    db = SessionLocal()
    item = db.query(DBItem).filter(DBItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": item}

@router.patch("/items/{item_id}")
def update_item(item_id: int, item: ItemUpdate, authenticated: bool = Depends(authenticate)):
    db = SessionLocal()
    db_item = db.query(DBItem).filter(DBItem.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.name = item.name
    db_item.quantity = item.quantity
    db.commit()
    db.refresh(db_item)
    return {"item": db_item}

@router.delete("/items/{item_id}")
def delete_item(item_id: int, authenticated: bool = Depends(authenticate)):
    db = SessionLocal()
    db_item = db.query(DBItem).filter(DBItem.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted"}
