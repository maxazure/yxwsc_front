from app import bcrypt, db
from .base_model import BaseModel


class User(BaseModel):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255))
    role_id = db.Column(db.Integer, default=0)
    mobile = db.Column(db.String(20), unique=True)
    avatar = db.Column(db.String(255))

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

   
    @staticmethod
    def find_by_id(id):
        return db.session.query(User).filter(
            User.id == id
        ).first()

    @staticmethod
    def find_by_username(username):
        return db.session.query(User).filter(
            User.username == username
        ).first()
