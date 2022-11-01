from sqlalchemy import func
from Tasks import db 
from hashlib import sha256
from datetime import datetime

class ExtraMixin(object):
    id=db.Column(db.Integer, primary_key=True)
    created_at= db.Column(db.DateTime, default=datetime.utcnow)
    updated_at= db.Column(db.DateTime , default=datetime.utcnow , onupdate=datetime.utcnow)
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
        
class Task(db.Model , ExtraMixin):
    __tablename__ = 'tasks'
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean, default=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    due_date = db.Column(db.DateTime)
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def get_by_user(cls, user_id):
        return cls.query.filter_by(created_by=user_id).all()
    
    @classmethod
    def get_user_tasks(cls, user_id):
        return cls.query.filter_by(created_by=user_id).all()
    
    
class User(db.Model , ExtraMixin):
    __tablename__ = 'users'
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)
    
    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_user_tasks(cls, user_id):
        return cls.query.filter_by(created_by=user_id).all()
    
    @classmethod
    def hash_password(cls, password):
        return sha256(password.encode()).hexdigest()
    
    @classmethod
    def verify_password(cls, password, hash):
        return sha256(password.encode()).hexdigest() == hash