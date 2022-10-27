from Todoapp.models import Todo
from flask_jwt_extended import jwt_required , get_jwt_identity
from flask_restful import Resource , reqparse
import datetime 


class Todo_resource(Resource):
    
    def __init__(self):
        self.parser = reqparse.RequestParser()
        
    # method post 
    @jwt_required()
    def post(self):
        self.parser.add_argument('title', type=str, required=True, help='This field cannot be blank')
        self.parser.add_argument('description', type=str, required=True, help='This field cannot be blank')
        # self.parser.add_argument('due_date', type=str, required=True, help='This field cannot be blank')
        self.parser.add_argument('complete', type=bool, required=True, help='This field cannot be blank')
        data = self.parser.parse_args()
        
        todo = Todo(
            **data,
            created_by=get_jwt_identity()['id'],
            due_date = datetime.datetime.now()
        )
        todo.save()
        
        return {'message': 'Todo created successfully'}, 201
