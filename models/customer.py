from sqlalchemy import ForeignKey, func
from app import db
from .base_model import BaseModel


class Customer(BaseModel):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    wechat_id = db.Column(db.String(60))
    credits = db.Column(db.Integer)
    default_addr_id = db.Column(db.Integer)
    vip_level = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, server_default=func.now())

    @staticmethod
    def find_by_id(id):
        return db.session.query(Customer).filter(
            Customer.id == id
        ).first()