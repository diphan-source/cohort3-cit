
class BaseConfig(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/cbs_news'
    SECRET_KEY = 'secret_key'
    
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


    