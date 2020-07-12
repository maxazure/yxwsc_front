from sqlalchemy import ForeignKey, func
from app import db
from .base_model import BaseModel


class Article(BaseModel):
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text)
    front_pic = db.Column(db.String(255))
    author = db.Column(db.String(80))
    is_header = db.Column(db.Boolean)
    is_col_header = db.Column(db.Boolean)
    catalog_id = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, server_default=func.now())

    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'front_pic': self.front_pic,
            'author': self.color.author,
            'is_header': self.color.is_header,
            'is_col_header': self.color.is_col_header,
            'inventcatalog_idory': self.inventcatalog_idory,
            'created_at': self.created_at
        }

    @staticmethod
    def find_by_id(id):
        return db.session.query(Article).filter(Article.id == id).first()
