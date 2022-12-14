from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager , login_user , logout_user , login_required , current_user
from flask_marshmallow import Marshmallow
import os
from flask_restful import  Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_mail import Mail
from sqlalchemy import MetaData



convention = {
    'xi': "ix_%(column_0_label)s",
    'pk': "pk_%(table_name)s" ,
    'ug': "uq_%(table_name)s_%(column_0_name)s",
    'ck': "ck_%(table_name)s_%(constraint_name)s",
    'fk': "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)
api = Api()
jwt = JWTManager()
mail = Mail()
cors = CORS()
migrate = Migrate()
ma = Marshmallow()
login_manager = LoginManager()



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    ma.init_app(app)
    mail.init_app(app)
    cors.init_app(app)
    jwt.init_app(app)
    api.init_app(app)
    
    
    from Todoapp.errors.handlers import errors
    
    app.register_blueprint(errors)
    
    # jwt headers required 
    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user['id']
    
    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        from Todoapp.models import User
        identity = jwt_data["sub"]
        return User.query.filter_by(id=identity).one_or_none()
    
    return app

from .auth import auth_routes
from .Todos import Todo_routes
from .users import user_routes

auth_routes(api)
Todo_routes(api)
user_routes(api)
