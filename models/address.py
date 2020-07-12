from sqlalchemy import ForeignKey, func
from app import db
from .base_model import BaseModel


class Address(BaseModel):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    province = db.Column(db.String(60))
    city = db.Column(db.String(60))
    detail = db.Column(db.String(255))
    district = db.Column(db.String(255))
    customer_id = db.Column(db.Integer)
    is_default = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, server_default=func.now())

    @staticmethod
    def find_by_id(id):
        return db.session.query(Address).filter(Address.id == id).first()
