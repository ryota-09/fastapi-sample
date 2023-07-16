from fastapi import FastAPI
from typing import Optional

from pydantic import BaseModel

class Item(BaseModel):
  name: str
  description: Optional[str] = None
  price: int
  tax: Optional[float] = None


app = FastAPI()

# 上から順番に当てはまるパスを探している

# /docs - swaggerUIのドキュメント, /redoc - Webページ用doc
@app.post("/countries/")
async def create_item(item: Item):
  return { "message": f"{item.name}の合計金額は{int(item.price * item.tax)}円です。" }
