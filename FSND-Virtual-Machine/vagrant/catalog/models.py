from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import insert, DateTime, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, UniqueConstraint
from flask_login import UserMixin
from . import db

class Genre(db.Model):
    __tablename__ = 'genre'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=False)

    tracks = db.relationship("Track", backref="genre")

    def __init__(self, name):
        self.name = name

class Track(db.Model):
    __tablename__ = 'track'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=False)
    slug = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 
    gen_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # user = relationship("User", backref="track")

    def __init__(self, name, slug, description, gen_id, user_id, date):
        self.name = name
        self.slug = slug
        self.description = description
        self.date = date
        self.gen_id = gen_id
        self.user_id = user_id


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), unique=True)

    tracks = relationship("Track", backref="user")

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        unicode = str
        try:
            return unicode(self.id)
        except AttributeError:
            raise NotImplementedError("No `id` attribute - override get_id")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User {}>'.format(self.username)
