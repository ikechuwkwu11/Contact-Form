from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
db = SQLAlchemy()

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100),nullable=False,unique=True)
    password = db.Column(db.String(50),nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)

class ContactMessage(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(50),nullable=False)
    subject = db.Column(db.String(100),nullable=False)
    message = db.Column(db.String(100),nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)