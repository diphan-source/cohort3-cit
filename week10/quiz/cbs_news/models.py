
from cbs_news import db
import datetime


# create the model class with common fields
class ExtraMixin(object):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self):
        db.session.commit()
        
# cbs_news model 
class CBSNews(db.Model, ExtraMixin):
    __tablename__ = 'cbs_news'
    
    title = db.Column(db.String(255))
    link = db.Column(db.String(255))
    image = db.Column(db.String(255))
    description = db.Column(db.Text)
    
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'link': self.link,
            'image': self.image,
            'description': self.description,
            'created_at': str(self.created_at)
        }
        
    @classmethod
    def get_all_news(cls):
        return cls.query.all()