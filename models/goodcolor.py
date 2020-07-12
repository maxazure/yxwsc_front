from sqlalchemy import ForeignKey, func
from app import db
from sqlalchemy.orm import relationship
from .base_model import BaseModel


class Goodcolor(BaseModel):
    __tablename__ = 'goodcolor'

    id = db.Column(db.Integer, primary_key=True)
    color_name = db.Column(db.String(60))
    color_thumbnail = db.Column(db.String(255))
    product_thumbnail = db.Column(db.String(255))
    good_id = db.Column(db.Integer)
    sizes = relationship('Goodsize', back_populates="color")

    created_at = db.Column(db.DateTime, server_default=func.now())

    @staticmethod
    def find_by_id(id):
        return db.session.query(Goodcolor).filter(Goodcolor.id == id).first()
