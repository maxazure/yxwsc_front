from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError
from sqlalchemy import or_, and_, text
from flask_jwt_extended import jwt_required
from models.user import User
from app import db
from utils.util import max_res

paginate_fields = {
    'total': fields.Integer,
    'pageSize': fields.Integer,
    'current': fields.Integer
}

user_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'username': fields.String,
    'email': fields.String,
    'role_id': fields.Integer,
    'mobile': fields.String,
    'avatar': fields.String,
}

user_list_fields = {
    'pagination': fields.Nested(paginate_fields),
    'list': fields.List(fields.Nested(user_fields)),
}
sortable_fields = ['id', 'name', 'email', 'mobile', 'role_id', 'username']

# parser of post for creating user
user_post_parser = reqparse.RequestParser()
user_post_parser.add_argument('name',
                              type=str,
                              required=True,
                              location=['json'],
                              help='name parameter is required')
user_post_parser.add_argument('username',
                              type=str,
                              required=True,
                              location=['json'],
                              help='username parameter is required')
user_post_parser.add_argument('email',
                              type=str,
                              required=True,
                              location=['json'],
                              help='email parameter is required')
user_post_parser.add_argument('password',
                              type=str,
                              required=True,
                              location=['json'],
                              help='password parameter is required')
user_post_parser.add_argument('role_id',
                              type=int,
                              required=True,
                              location=['json'],
                              help='role_id parameter is required')
user_post_parser.add_argument('mobile',
                              type=str,
                              required=True,
                              location=['json'],
                              help='mobile parameter is required')
user_post_parser.add_argument('avatar', type=str, location=['json'])

# parser of post for updating user
user_update_parser = reqparse.RequestParser()
user_update_parser.add_argument('name', type=str, location=['json'])
user_update_parser.add_argument('username', type=str, location=['json'])
user_update_parser.add_argument('email', type=str, location=['json'])
user_update_parser.add_argument('password', type=str, location=['json'])
user_update_parser.add_argument('role_id', type=int, location=['json'])
user_update_parser.add_argument('mobile', type=str, location=['json'])
user_update_parser.add_argument('avatar', type=str, location=['json'])

# parser of post for muti-query
user_query_parser = reqparse.RequestParser()
user_query_parser.add_argument('name', type=str)
user_query_parser.add_argument('username', type=str)
user_query_parser.add_argument('email', type=str)
user_query_parser.add_argument('mobile', type=str)
user_query_parser.add_argument('role_id', type=int, help='Invalid role_id')

user_query_parser.add_argument('orderby', type=str, default='id')
user_query_parser.add_argument('desc', type=int, default=0)
user_query_parser.add_argument('page', type=int)
user_query_parser.add_argument('pagesize', type=int)


class UsersResource(Resource):
    @jwt_required
    def get(self, user_id=None):
        if user_id:
            user = User.find_by_id(user_id)
            return max_res(marshal(user, user_fields))
        else:

            conditions = []
            args = user_query_parser.parse_args()
            page = args['page']
            per_page = args['pagesize']

            if args['name'] is not None:
                conditions.append(User.name.like('%' + args['name'] + '%'))
            if args['username'] is not None:
                conditions.append(
                    User.username.like('%' + args['username'] + '%'))
            if args['email'] is not None:
                conditions.append(User.email == args['email'])
            if args['mobile'] is not None:
                conditions.append(User.mobile == args['mobile'])
            if args['role_id'] is not None:
                conditions.append(User.role_id == args['role_id'])

            if args['orderby'] not in sortable_fields:
                return max_res('', code=500, errmsg='非法字段')
            sort = args['orderby']
            if args['desc'] > 0:
                sort = args['orderby'] + ' desc'

            if conditions is []:
                pagination = User.query.order_by(text(sort)).paginate(
                    page, per_page, error_out=False)
            else:
                pagination = User.query.filter(*conditions).order_by(
                    text(sort)).paginate(page, per_page, error_out=False)
            paginate = {
                'total': pagination.total,
                'pageSize': pagination.per_page,
                'current': pagination.page
            }

            return max_res(
                marshal(
                    {
                        'pagination': paginate,
                        'list':
                        [marshal(u, user_fields) for u in pagination.items]
                    }, user_list_fields))

    # TODO @jwt_required
    def post(self):
        args = user_post_parser.parse_args()
        password = args['password']

        user = User(name=args['name'],
                    username=args['username'],
                    email=args['email'],
                    role_id=args['role_id'],
                    mobile=args['mobile'],
                    avatar=args['avatar'])

        user.set_password(password)

        try:
            user.add()
        except IntegrityError:
            return max_res('', code=401, errmsg='用户已存在')

        return max_res(marshal(user, user_fields))

    @jwt_required
    def put(self, user_id=None):

        user = User.find_by_id(user_id)

        if not user:
            return max_res('', 500, 'Something went wrong.')

        args = user_update_parser.parse_args()

        if args['name']:
            user.name = args['name']
        if args['username']:
            user.username = args['username']
        if args['email']:
            user.email = args['email']
        if args['role_id'] is not None:
            user.role_id = args['role_id']
        if args['mobile']:
            user.mobile = args['mobile']
        if args['avatar']:
            user.avatar = args['avatar']
        if args['password']:
            user.set_password(args['password'])

        try:
            user.update()
        except Exception as e:
            return max_res('', 500, 'Failed to modify.')

        return max_res(marshal(user, user_fields))

    @jwt_required
    def delete(self, user_id=None):
        user = User.find_by_id(user_id)

        try:
            user.delete()
        except Exception as e:
            return max_res('', 500, 'The user has already deleted.')

        return max_res('The {} has been deleted.'.format(user.name))