from. import db 
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    upload = db.relationship('UploadFiles', backref='user')
   
  

class UploadFiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer, nullable=False)
    desc = db.Column(db.String(30),db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    catagory = db.Column(db.String(30), nullable=False)
    
    




class IncomeExpenses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(30), default='income', nullable=False)
    category = db.Column(db.String(30), default='rent', nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    amount = db.Column(db.Integer, nullable=False)

    def __str__(self):
        return self.id