from Tasks.models import Task , User
from flask_marshmallow import Schema
from flask_marshmallow.sqla import SQLAlchemyAutoSchema

        
class UserSchema(Schema):
    class Meta:
        field = ('id', 'name', 'email')
        

class TaskSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        include_fk = True
        load_instance = True
        