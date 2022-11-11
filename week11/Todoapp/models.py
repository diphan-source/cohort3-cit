
from datetime import datetime

from sqlalchemy import func
from Todoapp import db
from flask_login import UserMixin
import hashlib


class ExtraMin(object):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now())
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self):
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
        
class User(ExtraMin , db.Model):
    __tablename__ = 'users'
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    
    @classmethod
    def find_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def find_user_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    @staticmethod
    def verify_password(password, hashed_password):
        return hashlib.sha256(password.encode()).hexdigest() == hashed_password
    
    
class Todo(db.Model , ExtraMin):
    __tablename__ = 'todos'
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50), nullable=False)
    due_date = db.Column(db.DateTime, default=datetime.utcnow)
    complete = db.Column(db.Boolean, default=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    
    @classmethod
    def get_todos(cls):
        return cls.query.all()
    
    @classmethod
    def get_todo_id(cls, todo_id):
        return cls.query.filter_by(todo_id=todo_id).first()
    
    @classmethod
    def get_user_todo(cls, user_id):
        return cls.query.filter_by(created_by=user_id).all()