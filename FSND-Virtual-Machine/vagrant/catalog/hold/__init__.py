import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from sqlalchemy import create_engine, MetaData
# from sqlalchemy.orm import scoped_session, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base


db = SQLAlchemy()


# Set up onnect to database
# engine = create_engine(
#                         'sqlite:///music.db',
#                         convert_unicode=True
# )
# Sessions = scoped_session(sessionmaker(bind=engine))
# quesession = Sessions()

# Base = declarative_base()
# Base.metadata.bind = engine


def create_app():
    app = Flask(
                __name__,
                instance_relative_config=True
    )

    app.secret_key = 'GenKey'
    app.config['SECRET_KEY'] = 'GenKey'
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(basedir, 'music.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
