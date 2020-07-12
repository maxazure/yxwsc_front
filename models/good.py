from sqlalchemy import ForeignKey, func
from app import db
from .base_model import BaseModel


class Good(BaseModel):
    __tablename__ = 'good'

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255), nullable=False)
    product_sn = db.Column(db.String(80))
    type_sn = db.Column(db.String(80))
    gender = db.Column(db.Integer)
    material = db.Column(db.Text)
    original_price = db.Column(db.Float)
    onsale_price = db.Column(db.Float)
    vip_price = db.Column(db.Float)
    colors = db.Column(db.Text)
    sizes = db.Column(db.Text)
    carousels = db.Column(db.Text)
    main_pic = db.Column(db.String(255))
    produt_parameter = db.Column(db.Text)
    detail = db.Column(db.Text)
    category_id = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, server_default=func.now())

    @staticmethod
    def find_by_id(id):
        return db.session.query(Good).filter(Good.id == id).first()
