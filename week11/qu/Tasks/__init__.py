
import os
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from flask_mail import Mail 
from flask_jwt_extended import JWTManager



convention = {
    'pk': 'pk_%(table_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ix': 'ix_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
}

metadata = MetaData(naming_convention=convention)

cors = CORS()
migrate = Migrate()
api = Api()
mail = Mail()
jwt = JWTManager()
ma = Marshmallow()
db = SQLAlchemy(metadata=metadata)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tasks.db"
    app.config['SECRET_KEY'] = 'mysecretkey'
    db.init_app(app)
    ma.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)
    
    
    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user['id']

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        from Tasks.models import User
        identity = jwt_data["sub"]
        return User.query.filter_by(id=identity).one_or_none()
    
    return app 

from .auth import auth_routes
from .user import user_routes
from .user_tasks import task_routes

auth_routes(api)
user_routes(api)
task_routes(api)