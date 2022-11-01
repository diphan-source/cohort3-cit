from Tasks.models import User
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
)
from flask_restful import Resource, reqparse


class Login(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def post(self):
        self.parser.add_argument('email', type=str, required=True, help='This field cannot be left blank')
        self.parser.add_argument('password', type=str, required=True, help='This field cannot be left blank')

        data = self.parser.parse_args()

        user = User.query.filter_by(email=data['email']).first()

        if user and user.check_password(data['password']):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                       'message': 'Logged in as {}'.format(user.email),
                       'access_token': access_token,
                       'refresh_token': refresh_token
                   }, 200

        return {'message': 'Invalid credentials'}, 401
    

class Register(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def post(self):
        self.parser.add_argument('name', type=str, required=True, help='This field cannot be left blank')
        self.parser.add_argument('email', type=str, required=True, help='This field cannot be left blank')
        self.parser.add_argument('password', type=str, required=True, help='This field cannot be left blank')
        

        data = self.parser.parse_args()

        if User.find_by_email(data['email']):
            return {'message': 'User {} already exists'.format(data['email'])}

        new_user = User(
            name = data['name'],
            email = data['email'],
            password = User.hash_password(data['password'])
        )
        new_user.save()

        return {'message': 'User {} was created'.format(data['email'])}, 201