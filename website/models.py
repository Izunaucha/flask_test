from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import pymysql

db = SQLAlchemy()
#use flask;
#show tables;
#show columns from users;l
#select * from users;
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(255))

    def __init__(self,username,password):
        self.username = username
        self.password = self.create_password(password)

    def create_password(self,password):
        return generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password,password)

class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(255))
    
    def __init__(self,username,password):
        self.username = username
        self.password = self.create_password(password)

    def create_password(self,password):
        return generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password,password)
