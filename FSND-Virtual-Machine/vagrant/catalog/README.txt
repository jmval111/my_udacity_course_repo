pip install flask-sqlalchemy
pip install flask-migrate

db.metadata.clear()

~/GitHub/udacity-git-course/FSND-Virtual-Machine/vagrant/

create database:
>>> from catalog import db, create_app
db.create_all(app=create_app())

>>> from app import db, create_app
db.create_all(app=create_app())

python loadbase.py

from app import create_app
from models import db
db.create_all(app=create_app())

from models import init_db
init_db()

export FLASK_APP=catalog
export FLASK_ENV=development
export FLASK_DEBUG=1
flask run

export FLASK_APP=app
export FLASK_ENV=development
export FLASK_DEBUG=1
flask run