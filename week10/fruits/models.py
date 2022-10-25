from fruits import db 



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






