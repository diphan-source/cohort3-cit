from Tasks.models import User
from flask_jwt_extended import jwt_required , get_jwt_identity
from flask_restful import Resource, reqparse

from Tasks.schemas.schema_app import UserSchema

UserSchema = UserSchema()
UserSchema = UserSchema(many=True)

class Users(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        
    # http method to get user 
    @jwt_required
    def get(self , user_id=None):
        if user_id:
           if user_id != get_jwt_identity():
               return {'message': 'You cannot view this user'}, 403
            # get user by id
           user = User.query.filter_by(id=user_id).first()
           
           if not user:
               return {'message': 'User with id {} does not exit '.format(user_id)}, 404
           
           return UserSchema.dump(user) , 200
       
    #    get all users 
        users = User.query.all()
        return UserSchema.dump(users) , 200
           