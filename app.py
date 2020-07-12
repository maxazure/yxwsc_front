from flask import Flask, jsonify, request, json
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_migrate import Migrate

from werkzeug.exceptions import HTTPException, InternalServerError
from werkzeug.exceptions import default_exceptions

from config import app_config
from baseapi import BaseApi

config_name = 'development'
bcrypt = Bcrypt()

app = Flask(__name__)
api = BaseApi(app, catch_all_404s=True)
app.config.from_object(app_config[config_name])
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
bcrypt.init_app(app)

# from utils.error_handle import *
# for ex in default_exceptions:
#     app.register_error_handler(ex, handle_error)

from resources.articles import Articles, ArticleList
from resources.goods import Good, GoodSizes

# front

api.prefix = '/api/v1/'
api.add_resource(ArticleList, '/articles/list/<int:catalog_id>')
api.add_resource(Articles, '/articles/<int:article_id>')
# api.add_resource(Good, '/goods/<int:good_id>')
# api.add_resource(GoodSizes, '/goodsizes/<int:good_id>')

if __name__ == '__main__':
    app.run()