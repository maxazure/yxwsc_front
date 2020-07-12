from sqlalchemy import ForeignKey, func
from app import db
from .base_model import BaseModel


class Orderitem(BaseModel):
    __tablename__ = 'orderitem'

    id = db.Column(db.Integer, primary_key=True)
    good_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    total = db.Column(db.Float)
    goodorder_id = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, server_default=func.now())

    @staticmethod
    def find_by_id(id):
        return db.session.query(Orderitem).filter(
            Orderitem.id == id
        ).first()