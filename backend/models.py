from flask_sqlalchemy import SQLAlchemy
from config import *
db = SQLAlchemy(Config)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    address = db.Column(db.String(1000), nullable = False)

class Professional(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    address = db.Column(db.String(1000), nullable = False)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(100), nullable = False)


    