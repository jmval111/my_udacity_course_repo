from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import DateTime, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, UniqueConstraint
from flask_login import UserMixin

Base = declarative_base()

class Genre(Base):
    __tablename__ = 'genre'

    idSSS = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)

    tracks = relationship("Track", backref="genre")

    def __init__(self, name):
        self.name = name

class Track(Base):
    __tablename__ = 'track'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    slug = Column(String(250), nullable=False)
    description = Column(String(250))
    date = Column(DateTime, nullable=False, default=datetime.utcnow) 
    gen_id = Column(Integer, ForeignKey('genre.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    # user = relationship("User", backref="track")

    def __init__(self, name, slug, description, gen_id, user_id, date):
        self.name = name
        self.slug = slug
        self.description = description
        self.date = date
        self.gen_id = gen_id
        self.user_id = user_id


class User(Base, UserMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), unique=True)

    tracks = relationship("Track", backref="user")

    created_on = Column(DateTime,
                        index=False,
                        unique=False,
                        nullable=True)
    last_login = Column(DateTime,
                        index=False,
                        unique=False,
                        nullable=True)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User {}>'.format(self.username)

db = 'sqlite:///music.db'
engine = create_engine(db)
Base.metadata.create_all(engine)
