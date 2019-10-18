from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
# from sqlalchemy import insert
from sqlalchemy.orm import relationship
from flask_login import UserMixin
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
from app import db  # , quesession


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

    def __init__(self, name, slug, description, gen_id):
        self.name = name
        self.slug = slug
        self.description = description
        self.gen_id = gen_id


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
        return '<User {}>'.format(self.name)


# if __name__ == '__main__':
#     db.metadata.clear()
#    db.create_all(app=create_app())

#    gen_list = Genre[
#        {"name": "Blues"},
#        {"name": "Classical"},
#        {"name": "Rock"},
#        {"name": "Hip-hop"},
#        {"name": "Country"},
#        {"name": "Funk"},
#        {"name": "Pop"},
#        {"name": "Reggae"},
#        {"name": "RnB"}
#    ]

#    runn = engine.execute(insert(Genre), gen_list)
#    runn.rowcount

#     # Load in basic Genres
#     # gen_list = Genre[
#     #     "Blues",
#     #     "Classical",
#     #     "Rock",
#     #     "Hip-hop",
#     #     "Country",
#     #     "Funk",
#     #     "Pop",
#     #     "Reggae",
#     #     "RnB"
#     # ]


#     g1 = Genre("Blues")
#     db.session.add(g1)
#     db.session.commit()
#     g2 = Genre("Classical")
#     db.session.add(g2)
#     db.session.commit()
#     g3 = Genre("Rock")
#     db.session.add(g3)
#     db.session.commit()
#     g4 = Genre("Hip-hop")
#     db.session.add(g4)
#     db.session.commit()
#     g5 = Genre("Country")
#     db.session.add(g5)
#     db.session.commit()
#     g6 = Genre("Funk")
#     db.session.add(g6)
#     db.session.commit()
#     g7 = Genre("Pop")
#     db.session.add(g7)
#     db.session.commit()
#     g8 = Genre("Reggae")
#     db.session.add(g8)
#     db.session.commit()
#     g9 = Genre("RnB")
#     db.session.add(g9)
#     db.session.commit()

#     # Create a test user
#     admin_user = User('admin', 'admin@email.com', 'password')
#     admin_user.display_name = 'Admin'
#     db.session.add(admin_user)
#     db.session.commit()


# if __name__ == "__main__":
#     db.create_all()

# Set up onnect to database
# engine = create_engine(
#                         'sqlite:///music.db',
#                         convert_unicode=True
# )
# Sessions = scoped_session(sessionmaker(bind=engine))
# quesession = Sessions()

# g1 = Genre("Blues")
# quesession.add(g1)
# quesession.commit()
# g2 = Genre("Classical")
# quesession.add(g2)
# quesession.commit()
# g3 = Genre("Rock")
# quesession.add(g3)
# quesession.commit()
# g4 = Genre("Hip-hop")
# quesession.add(g4)
# quesession.commit()
# g5 = Genre("Country")
# quesession.add(g5)
# quesession.commit()
# g6 = Genre("Funk")
# quesession.add(g6)
# quesession.commit()
# g7 = Genre("Pop")
# quesession.add(g7)
# quesession.commit()
# g8 = Genre("Reggae")
# quesession.add(g8)
# quesession.commit()
# g9 = Genre("RnB")
# quesession.add(g9)
# quesession.commit()

# # Create a test user
# admin_user = User('admin', 'admin@email.com', 'password*7#')
# admin_user.display_name = 'Admin'
# quesession.add(admin_user)
# quesession.commit()
