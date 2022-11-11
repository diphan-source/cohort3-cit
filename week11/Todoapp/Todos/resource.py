from Todoapp.models import Todo
from flask_jwt_extended import jwt_required , get_jwt_identity
from flask_restful import Resource , reqparse
import datetime 
from Todoapp.schemas.app_schemas import TodoSchema

todo_schema = TodoSchema()
todo_schema = TodoSchema(many=True)

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
    
    @jwt_required
    def get_todos(self , todo_id = None):
        if todo_id:
            todo = Todo.get_todo_id(todo_id)
            if todo:
                return todo_schema.dump(todo)
            return {'message': 'Todo not found'}, 404
        
        user_id = get_jwt_identity()['id']
        user_todos = Todo.get_user_todos(user_id)
        return todo_schema.dump(user_todos)
    
    @jwt_required
    def put(self , todo_id):
        # while updating the todos the fields are optional 
        self.parser.add_argument('title', type=str)
        self.parser.add_argument('description', type=str)
        self.parser.add_argument('due_date', type=str)
        self.parser.add_argument('complete', type=bool)
        
        todo = Todo.get_todo_id(todo_id)
        
        if not todo:
            return {'message': 'Todo not found'}, 404
        
        # check ownership of the todo
        if todo.created_by != get_jwt_identity()['id']:
            return {'message': 'You are not authorized to update this todo'}, 403
        
        data = self.parser.parse_args()
        
        # update todos if there is a new todo 
        todo.title = data['title'] if data['title'] else todo.title
        todo.description = data['description'] if data['description'] else todo.description
        todo.due_date = datetime.strptime(data['due_date'], '%Y-%m-%d') if data['due_date'] else todo.due_date
        todo.complete = data['complete'] if data['complete'] else todo.complete
        todo.update()
        
        # return the updated todo
        return todo_schema.dump(todo)
    
    
    @jwt_required
    def delete(self , todo_id):
        todo = Todo.get_todo_id(todo_id)
        
        if not todo:
            return {'message': 'Todo not found'}, 404
        
        # check ownership of the todo
        if todo.created_by != get_jwt_identity()['id']:
            return {'message': 'You are not authorized to delete this todo'}, 403
        
        todo.delete()
        return {'message': 'Todo deleted successfully'}, 200