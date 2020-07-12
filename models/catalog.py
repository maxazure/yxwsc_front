from sqlalchemy import ForeignKey, func
from app import db
from .base_model import BaseModel


class Catalog(BaseModel):
    __tablename__ = 'catalog'

    id = db.Column(db.Integer, primary_key=True)
    catalog_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    parent_id = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, server_default=func.now())

    @staticmethod
    def find_by_id(id):
        return db.session.query(Catalog).filter(
            Catalog.id == id
        ).first()