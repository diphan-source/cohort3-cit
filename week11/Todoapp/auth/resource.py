
from sqlalchemy import Identity
from Todoapp.models import User 
from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)

# @view.route('/login', methods=['POST'])

# use class based view in flask_restful
class Login(Resource):
    
    def __init__(self):
        self.parser = reqparse.RequestParser()
    
    # http method for login (post)
    def post(self):
        self.parser.add_argument('email', type=str, required=True, help='This field cannot be blank')
        self.parser.add_argument('password', type=str, required=True, help='This field cannot be blank')
        data = self.parser.parse_args()
        
    
        # check if user exists
        user = User.find_user_by_email(data['email'])
        print(user)
        
        if user and User.verify_password(data['password'], user.password):
            
            identity = {'id': user.id, 'email': user.email}
            access_token = create_access_token(identity=identity)
            refresh_token = create_refresh_token(identity=identity)
            return {
                'message': 'Logged in as {}'.format(user.email),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        return {'message': 'Invalid credentials'}, 401
    
    
class Register(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    # http method: post
    def post(self):
        self.parser.add_argument('name', type=str, required=True, help='Name cannot be blank')
        self.parser.add_argument('email', type=str, required=True, help='Email cannot be blank')
        self.parser.add_argument('password', type=str, required=True, help='Password cannot be blank')

        data = self.parser.parse_args()

        if User.find_user_by_email(data['email']):
            return {'message': 'User with {} already exists'.format(data['email'])}, 400

        new_user = User(
            name=data['name'],
            email=data['email'],
            password=User.hash_password(data['password'])
        )
        new_user.save()
        return {'message': 'User {} was created'.format(data['email'])}, 201
