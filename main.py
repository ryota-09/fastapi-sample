from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# 上から順番に当てはまるパスを探している

# /docs - swaggerUIのドキュメント, /redoc - Webページ用doc
@app.get("/countries/")
async def country(country_name: Optional[str] = None, country_no: Optional[int] = None):
  return { "country_name": country_name, "country_no": country_no }
