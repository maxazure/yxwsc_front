from datetime import date, datetime, time
from sqlalchemy import ForeignKey, func
from app import db
from .base_model import BaseModel



class Category(BaseModel):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    parent_id = db.Column(db.Integer, default=0)
    sort = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, server_default=func.now())

    @staticmethod
    def find_by_id(id):
        return db.session.query(Category).filter(
            Category.id == id
        ).first()