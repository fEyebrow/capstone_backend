import os
from sqlalchemy import Column, String, Integer, DateTime
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "capstone"
database_path = "postgres://fourfish@{}/{}".format(
    'localhost:5432', database_name)

if "DATABASE_URL" in os.environ:
    database_path = os.environ['DATABASE_URL']
db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


'''
Drink
a persistent drink entity, extends the base SQLAlchemy Model
'''


class Movie(db.Model):
    __tablename__ = 'movie'
    id = Column(db.Integer, primary_key=True)
    title = Column(String(80), nullable=True)
    date = Column(DateTime)

    def long(self):
        return {
            'id': self.id,
            'title': self.title,
            'date': self.date.timestamp()*1000.0
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

class Actor(db.Model):
    __tablename__ = 'actor'
    id = Column(db.Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    age = Column(db.Integer)
    gender = Column(db.Integer)

    def long(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
