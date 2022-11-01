from Tasks.models import Task
from flask_jwt_extended import jwt_required , get_jwt_identity
from flask_restful import Resource, reqparse
from datetime import datetime

from Tasks.schemas.schema_app import TaskSchema

Task_schema = TaskSchema()
Tasks_schema = TaskSchema(many=True)

# Tasks Resource
class TaskResource(Resource):
    @jwt_required
    def get(self, task_id=None):
        if task_id:
            task = Task.get_by_id(task_id)
            return Task_schema.dump(task)
        else:
            user_id = get_jwt_identity()
            tasks = Task.get_user_tasks(user_id)
            return Tasks_schema.dump(tasks)

    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, help='This field cannot be left blank')
        parser.add_argument('description', type=str, required=True, help='This field cannot be left blank')
        parser.add_argument('completed', type=bool, required=True, help='This field cannot be left blank')
        parser.add_argument('due_date', type=str, required=True, help='This field cannot be left blank')
        
        
        data = parser.parse_args()
            
        # create date object from string needed by sqlite db 
        data['due_date'] = datetime.strptime(data['due_date'], '%Y-%m-%d')
        
        user_id = get_jwt_identity()
        
        new_task = Task(**data, created_by=user_id)
        new_task.save()
        return {'message': 'Task created successfully'}, 201
            

    @jwt_required
    def delete(self, task_id):
        task = Task.get_by_id(task_id)
        
        # check if task exists
        if not task:
            return {'message': 'Task not found'}, 404
        
        # check ownership
        if task.created_by != get_jwt_identity():
            return {'message': 'You cannot delete this task'}, 401
        
        task.delete()
        return {'message': 'Task deleted successfully'}, 200


    @jwt_required
    def put(self , task_id):
        # updating all fields are optional 
        parser = reqparse.RequestParser()
        self.parser.add_argument('title', type=str )
        self.parser.add_argument('description', type=str )
        self.parser.add_argument('completed', type=bool )
        self.parser.add_argument('due_date', type=str )
        
        task = Task.get_by_id(task_id)
        
        if not task:
            return {'message': 'Task not found'}, 404
        
        # check for ownership
        if task.created_by != get_jwt_identity():
            return {'message': 'You are not authorized to update this task '}, 401
        
        data = parser.parse_args()
        
        # update only the fields that are passed in the request
        task.title = data['title'] if data['title'] else task.title
        task.description = data['description'] if data['description'] else task.description
        task.completed = data['completed'] if data['completed'] else task.completed
        task.due_date = datetime.strptime(data['due_date'], '%Y-%m-%d') if data['due_date'] else task.due_date
        
        task.update()
        return {'message': 'Task updated successfully'}, 200