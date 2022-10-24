
# create the configuration class 
class BaseConfig(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/cbs_news'
    
class ProductionConfig(BaseConfig):
    DEBUG = False
    
class DevelopmentConfig(BaseConfig):
    DEBUG = True
    
class TestingConfig(BaseConfig):
    TESTING = True
    
    
app_config = {
    'development': DevelopmentConfig,
    "production": ProductionConfig,
    'testing': TestingConfig
}


    