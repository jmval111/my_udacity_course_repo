
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
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

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.secret_key = 'GenKey'
    app.config['SECRET_KEY'] = 'GenKey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

if __name__ == '__main__':
    init_db()
