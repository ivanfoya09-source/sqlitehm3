from typing import Optional

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Float, Boolean, Integer

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id: int = db.Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name: str = db.Column(String(50), nullable=False)
    email: Optional[str] = db.Column(String(255), unique=True, nullable=True)
    active: bool = db.Column(Boolean(), default=True)

class Event(db.Model):
    __tablename__ = "events"
    id: int = db.Column(Integer, primary_key=True, autoincrement=True, unique=True)
    title: str = db.Column(String(100), nullable=False)
    date: Optional[str] = db.Column(String(20), nullable=True)

class Ticket(db.Model):
    __tablename__ = "tickets"
    id: int = db.Column(Integer, primary_key=True, autoincrement=True, unique=True)
    user_id: int = db.Column(Integer, nullable=False) 
    event_id: int = db.Column(Integer, nullable=False)
    price: float = db.Column(Float, nullable=False)