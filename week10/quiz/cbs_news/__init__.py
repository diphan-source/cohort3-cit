
from flask import Flask 
from .config import app_config 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
from flask_marshmallow import Marshmallow 
import os 

# initialize the database 
db = SQLAlchemy() 


# initialize migrate 
migrate= Migrate() 

# initialize marshmallow 
ma = Marshmallow() 

TEMPLATES_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates') 

# create the instance of the flask app 

def create_app(): 
    app = Flask(__name__, template_folder=TEMPLATES_FOLDER) 
    app.config.from_object(app_config['development']) 
    db.init_app(app) 
    ma.init_app(app) 
    migrate.init_app(app,db) 
    
    from .views.cbs_views import cbs_views as cbs_news
    
    app.register_blueprint(cbs_news) 
    
    return app