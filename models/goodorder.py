from sqlalchemy import ForeignKey, func
from app import db
from .base_model import BaseModel


class Goodorder(BaseModel):
    __tablename__ = 'goodorder'

    id = db.Column(db.Integer, primary_key=True)
    cusutomer_id = db.Column(db.Integer)
    total_amount = db.Column(db.Float)

    created_at = db.Column(db.DateTime, server_default=func.now())

    @staticmethod
    def find_by_id(id):
        return db.session.query(Goodorder).filter(
            Goodorder.id == id
        ).first()