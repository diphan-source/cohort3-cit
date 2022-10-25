from fruits import db 
import hashlib


class ExtraMixin(object):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self):
        db.session.commit()
        
        
# fruits model 
class Fruit(db.Model, ExtraMixin):
    __tablename__ = 'fruits'
    name = db.Column(db.String(50), nullable=False)
    color = db.Column(db.Float, nullable=False)
    price = db.Column(db.String(100), nullable=False)
    
    def __init__(self, name, color , price):
        self.name = name
        self.color = color
        self.price = price
        
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
class HackerNews(db.Model, ExtraMixin):
    __tablename__ = 'hacker_news'
    title = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'link': self.link,
            'created_at': str(self.created_at),
        }

    

    @classmethod
    def get_all_news(cls):
        return cls.query.all()


class User(db.Model, ExtraMixin):
    __tablename__ = 'users'
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
   
    # hash password
    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    # verify password
    @staticmethod
    def verify_password(password, hashed_password):
        return User.hash_password(password) == hashed_password
    
    # select * from users where email = email
    @classmethod
    def get_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    # select * from users where username = username
    @classmethod
    def get_user_by_username(cls, username):
        return cls.query.filter_by(username=username).first()