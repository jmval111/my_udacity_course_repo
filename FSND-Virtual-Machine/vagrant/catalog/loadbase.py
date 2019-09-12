from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker
from models import Base, Genre, Track, User

engine = create_engine('sqlite:///music.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# This Json list adds the Genres to the database.
gen_list = [
    {
        "name"  : "Blues"
    },
    {
        "name" : "Classical"
    },
    {
        "name" : "Rock"
    },
    {
        "name" : "Hip-hop"
    },
    {
        "name" : "Country"
    },
    {
        "name" : "Funk"
    },
    {
        "name" : "Pop"
    },
    {
        "name" : "Reggae"
    },
    {
        "name" : "RnB"
    }
]

# This Json list adds the track
track_list = [
    {
        "name" : "Hoochi Choochi Man",
        "slug" : "hoochi-choochi-man",
        "description" : '''
                        "Hoochie Coochie Man" (originally titled "I'm Your Hoochie Cooche Man") is a blues standard written by Willie Dixon and first recorded by Muddy Waters in 1954. The song makes reference to hoodoo folk magic elements and makes novel use of a stop-time musical arrangement. It became one of Waters' most popular and identifiable songs and helped secure Dixon's role as Chess Records' chief songwriter.
                        ''',
        "gen_id" : 1, 
        "user_id" : 1
    },
    {
        "name" : "Nine Below Zero",
        "slug" : "nine-below-zero",
        "description" : "This is where the information goes.",
        "gen_id" : 1, 
        "user_id" : 1
    },
    {
        "name" : "Blues 3",
        "slug" : "blues-3",
        "description" : "This is where the information goes.",
        "gen_id" : 1, 
        "user_id" : 1
    },
    {
        "name" : "Flight of the Bumblebee",
        "slug" : "flight-of-the-bumblebee",
        "description" : "This is where the information goes.",
        "gen_id" : 2, 
        "user_id" : 1
    },
    {
        "name" : "Classical 2",
        "slug" : "classical-2",
        "description" : "This is where the information goes.",
        "gen_id" : 2, 
        "user_id" : 1
    },
    {
        "name" : "Achy Breaky Heart",
        "slug" : "achy-breaky-heart",
        "description" : "This is where the information goes.",
        "gen_id" : 5, 
        "user_id" : 1
    },
    {
        "name" : "The Devil Went Down to Georgia",
        "slug" : "the-devel-wenth-down-to-georgia",
        "description" : "This is where the information goes.",
        "gen_id" : 5, 
        "user_id" : 1
    },
    {
        "name" : "Funk 1",
        "slug" : "funk-1",
        "description" : "This is where the information goes.",
        "gen_id" : 6, 
        "user_id" : 1
    },
    {
        "name" : "Funk 2",
        "slug" : "funk-2",
        "description" : "This is where the information goes.",
        "gen_id" : 6, 
        "user_id" : 1
    },
    {
        "name" : "Funk 3",
        "slug" : "funk-4",
        "description" : "This is where the information goes.",
        "gen_id" : 6, 
        "user_id" : 2
    },
    {
        "name" : "Funk 4",
        "slug" : "funk-4",
        "description" : "This is where the information goes.",
        "gen_id" : 6, 
        "user_id" : 2
    },
    {
        "name" : "The Food",
        "slug" : "the-food",
        "description" : "This is where the information goes.",
        "gen_id" : 4, 
        "user_id" : 2
    },
    {
        "name" : "HipHop 2",
        "slug" : "hiphop-2",
        "description" : "This is where the information goes.",
        "gen_id" : 4, 
        "user_id" : 2
    },
    {
        "name" : "Hipop 3",
        "slug" : "hiphop-3",
        "description" : "This is where the information goes.",
        "gen_id" : 4, 
        "user_id" : 2
    },
    {
        "name" : "HipHop 4",
        "slug" : "hiphop-4",
        "description" : "This is where the information goes.",
        "gen_id" : 4, 
        "user_id" : 2
    },
    {
        "name" : "Reggae 1",
        "slug" : "reggae-1",
        "description" : "This is where the information goes.",
        "gen_id" : 8, 
        "user_id" : 1
    },
    {
        "name" : "Reggae 2",
        "slug" : "reggae-2",
        "description" : "This is where the information goes.",
        "gen_id" : 8, 
        "user_id" : 1
    },
    {
        "name" : "Pop 1",
        "slug" : "pop-1",
        "description" : "This is where the information goes.",
        "gen_id" : 7, 
        "user_id" : 1
    },
    {
        "name" : "Pop 2",
        "slug" : "pop-2",
        "description" : "This is where the information goes.",
        "gen_id" : 7, 
        "user_id" : 1
    },
    {
        "name" : "Pop 3",
        "slug" : "pop-3",
        "description" : "This is where the information goes.",
        "gen_id" : 7, 
        "user_id" : 1
    },
    {
        "name" : "Pop 4",
        "slug" : "pop-4",
        "description" : "This is where the information goes.",
        "gen_id" : 7, 
        "user_id" : 1
    },
    {
        "name" : "RnB 1",
        "slug" : "rnb-1",
        "description" : "This is where the information goes.",
        "gen_id" : 9, 
        "user_id" : 2
    },
    {
        "name" : "RnB 2",
        "slug" : "rnb-2",
        "description" : "This is where the information goes.",
        "gen_id" : 9, 
        "user_id" : 2
    },
    {
        "name" : "RnB 3",
        "slug" : "rnb-3",
        "description" : "This is where the information goes.",
        "gen_id" : 9, 
        "user_id" : 2
    },
    {
        "name" : "RnB 4",
        "slug" : "rnb-4",
        "description" : "This is where the information goes.",
        "gen_id" : 9, 
        "user_id" : 2
    },
    {
        "name" : "RnB 5",
        "slug" : "rnb-5",
        "description" : "This is where the information goes.",
        "gen_id" : 9, 
        "user_id" : 2
    },
    {
        "name" : "RnB 6",
        "slug" : "rnb-6",
        "description" : "This is where the information goes.",
        "gen_id" : 9, 
        "user_id" : 2
    }
]

# This Json list adds the user
user_list = [
    {
        "name" : "admin",
        "email" : "email@this.com",
        "password" : "password"
    },
    {
        "name" : "admin2",
        "email" : "email2@this.com",
        "password" : "password2"
    }
]

runn = engine.execute(insert(Genre), gen_list)
runn.rowcount
drive = engine.execute(insert(Track), track_list)
drive.rowcount
store = engine.execute(insert(User), user_list)
store.rowcount

print("Tracks are added!")
