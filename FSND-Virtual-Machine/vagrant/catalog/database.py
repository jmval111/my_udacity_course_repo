from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///music.db', \
                        convert_unicode=True)
Sessions = scoped_session(sessionmaker(autocommit=False,
                                        autoflush=False,
                                        bind=engine))
quesession = Sessions()

Base = declarative_base()
Base.metadata.bind = engine

def init_db():
    from models import Genre, Track, User
    Base.metadata.create_all(bind=engine)
