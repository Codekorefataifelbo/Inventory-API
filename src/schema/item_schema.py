from pydantic import BaseModel, Field
from typing import Optional

class Item(BaseModel):
    name: str
    quantity: int

class ItemUpdate(BaseModel):
    name: Optional[str] = Field(None, description="Optional name of the item")
    quantity: Optional[int] = Field(None, description="Optional quantity of the item")
