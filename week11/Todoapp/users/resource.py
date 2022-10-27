from Todoapp.models import User
from flask_jwt_extended import jwt_required , get_jwt_identity
from flask_restful import Resource , reqparse
from Todoapp.schemas.app_schemas import UserSchema


class Users(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser
        
        
    #  method GET 
    @jwt_required()
    def get(self , user_id = None):
        if user_id:
            if not user_id == get_jwt_identity():
                return {'message': 'You can only view your own profile'}, 403
            
            #  get asingle user 
            user = User.query.filter_by(id=user_id).first()
            if not user:
                return {'message': 'User not found'}, 404
            
            return UserSchema.dump(user), 200
        
        # get all users
        users = user.query.all()
        return UserSchema.dump(users, many=True), 200 