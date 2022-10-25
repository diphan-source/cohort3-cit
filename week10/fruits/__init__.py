
from re import TEMPLATE
from flask import Flask 
from .config import app_config
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import os

# db variable initialization
db = SQLAlchemy()



# create an instance of the flask app
app = Flask(__name__)

# initialize migration
migrate= Migrate()

# initialize marshmallow
ma = Marshmallow()



TEMPLATES_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
STATIC_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')


def create_app():
    app = Flask(__name__, template_folder=TEMPLATES_FOLDER)
    app.config.from_object(app_config['development'])
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app,db)
    
    
    from .views.fruits_view import views as fruits_views
    from .views.hacker_news import hviews as hacker_news_views
    
    app.register_blueprint(fruits_views)
    app.register_blueprint(hacker_news_views)
    
    return app