from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from sqlalchemy.exc import IntegrityError
from sqlalchemy import or_, and_, text
from flask_jwt_extended import jwt_required
from models.article import Article
from app import db
from utils.util import max_res


class Articles(Resource):
    def get(self, article_id=None):
        article = Article.find_by_id(article_id)
        res = {
            'id': article.id,
            'title': article.title,
            'body': article.body,
            'front_pic': article.front_pic
        }
        return max_res(res)


class ArticleList(Resource):
    def get(self, catalog_id=None):

        conditions = []
        conditions.append(Article.catalog_id == catalog_id)

        res = Article.query.filter(*conditions).all()

        temp = []
        for item in res:
            temp.append({
                'id': item.id,
                'title': item.title,
                'author': item.author
            })

        return max_res(temp)

    def post(self):
        pass