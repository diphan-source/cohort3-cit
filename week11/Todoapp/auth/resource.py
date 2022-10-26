
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
        
        return {'message': 'Login page'}
        
        user = User.find_user_by_email(data['email'])
        
        if user and User.verify_password(data['password'], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                'message': 'Logged in as {}'.format(user.email),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        return {'message': 'Invalid credentials'}, 401