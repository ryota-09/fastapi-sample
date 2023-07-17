from sqlalchemy.orm import Session
from . import models, schemas

# ユーザー一覧を取得.
def get_users(db: Session, skip: int = 0, limit: int = 100):
  return db.query(models.User).offset(skip).limit(limit).all()

# 会議室一覧取得
def get_rooms(db: Session, skip: int = 0, limit: int = 100):
  return db.query(models.room).offset(skip).limit(limit).all()

# 予約一覧
def get_bookings(db: Session, skip: int = 0, limit: int = 100):
  return db.query(models.booking).offset(skip).limit(limit).all()

