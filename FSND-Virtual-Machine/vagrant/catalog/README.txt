pip install flask-sqlalchemy
pip install flask-migrate


~/GitHub/udacity-git-course/FSND-Virtual-Machine/vagrant/

create database:
    >>> from catalog import db, create_app
    >>> db.create_all(app=create_app())

export FLASK_APP=catalog
export FLASK_ENV=development
export FLASK_DEBUG=1
flask run