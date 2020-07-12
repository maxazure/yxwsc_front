from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import relationship
from app import db
from .base_model import BaseModel


class Goodsize(BaseModel):
    __tablename__ = 'goodsize'

    id = db.Column(db.Integer, primary_key=True)
    size_name = db.Column(db.String(60))
    display_name = db.Column(db.String(69))
    description = db.Column(db.String(255))

    inventory = db.Column(db.Integer)
    good_id = db.Column(db.Integer)

    color_id = db.Column(db.Integer, ForeignKey('goodcolor.id'))
    color = relationship('Goodcolor', back_populates="sizes")

    created_at = db.Column(db.DateTime, server_default=func.now())

    def json(self):
        return {
            'id': self.id,
            'size_name': self.size_name,
            'display_name': self.display_name,
            'description': self.description,
            'inventory': self.inventory,
            'good_id': self.good_id,
            'color_id': self.color.id,
            'color_name': self.color.color_name
        }

    @staticmethod
    def find_by_id(id):
        return db.session.query(Goodsize).filter(Goodsize.id == id).first()
