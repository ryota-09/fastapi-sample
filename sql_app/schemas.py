from fastapi import FastAPI
from pydantic import BaseModel, Field
import datetime

class Booking(BaseModel):
  booking_id: int
  user_id: int
  booked_num:int
  start_datetime: datetime.datetime
  end_datetime: datetime.datetime
  # pydanticの仕様(orm対応)
  class Config:
    orm_mode = True
  
class User(BaseModel):
  user_id: int
  user_name: str = Field(max_length=12)
  
  class Config:
    orm_mode = True

class Room(BaseModel):
  room_id: int
  room_name: str = Field(max_length=12)
  capacity: int
  
  class Config:
    orm_mode = True
