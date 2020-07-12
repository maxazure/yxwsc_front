from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from sqlalchemy.exc import IntegrityError
from sqlalchemy import or_, and_, text
from flask_jwt_extended import jwt_required
from models.goodsize import Goodsize
from models.goodcolor import Goodcolor
from app import db
from utils.util import max_res
import json


class Good(Resource):
    def get(self, good_id=None):
        conditions = []
        conditions.append(Goodsize.good_id == good_id)
        good = Goodsize.query.filter(*conditions).first()
        return max_res(good.json())


class GoodSizes(Resource):
    def get(self, good_id=None):
        conditions = []
        conditions.append(Goodsize.good_id == good_id)
        res = Goodsize.query.filter(*conditions).all()

        temp = []
        for item in res:
            temp.append(item.json())
        return max_res(temp)
