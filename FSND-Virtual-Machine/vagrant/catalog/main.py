#! /usr/bin/python3

from .models import User, Genre, Track
from flask import Flask, Blueprint, session, render_template, redirect, url_for, \
    request, flash, jsonify
from sqlalchemy import create_engine, desc, func, select
from sqlalchemy.orm import sessionmaker, scoped_session
from werkzeug.security import generate_password_hash, \
    check_password_hash
from flask_login import LoginManager, login_user, logout_user, \
    login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from . import quesession

main = Blueprint('main', __name__)

# Views 
@main.route("/")
@main.route("/songbase/")
def home():
    genre = Genre.query.order_by(desc(Genre.name))
    track = Track.query.order_by(desc(Track.date)).limit(5)
    return render_template('views/home.html', genre=genre, track=track)

# Show all tracks availiable within selected Genre <genre.name>/
@main.route('/songbase/<path:genre_name>/<int:genre_id>')
def showTracks(genre_name, genre_id):
    gen_title = Genre.query.\
                filter(Genre.id == genre_id)
    track = Track.query.\
            filter(Track.gen_id == genre_id).\
                order_by(desc(Track.date)).all()
    trk_count = Track.query.\
                filter(Track.gen_id == genre_id).count()#.all()
    full = Genre, Track.query.filter(Track.gen_id == genre_id).all()
    return render_template('views/tracks.html', gen_title=gen_title,\
                            track=track, trk_count=trk_count, full=full)

# Show selected track infromation <genre_name>/<track_name>/
@main.route('/songbase/<path:genre_name>/<path:track_name>/<int:track_id>') 
def trackInfo(genre_name, track_name, track_id):
    genre = Genre.query.\
            filter(Genre.name == genre_name)
    track = Track.name.query.\
            filter(Track.slug == track_name).all()
    full = Track.description.query.\
           filter(Track.id == track_id).all()
    return render_template('views/info.html', genre=genre, track=track, full=full)

@main.route('/songbase/add-genre')
def addGenre():
    genre = Genre.query.all()
    track = Track.query.all()
    return render_template('views/add-genre.html', genre=genre, track=track)
    # return "page to add a track. Task 1 complete!"

# Set route for addTrack function here
@main.route('/songbase/add-track')
def addTrack():
    genre = Genre.query.all()
    track = Track.query.all()
    return render_template('views/add-track.html', genre=genre, track=track)
    # return "page to add a track. Task 1 complete!"

# Set route for editTrack function here
@main.route('/songbase/genre/<int:genre_id>/track/<int:track_id>/edit/') 
def editTrack(genre_id, track_id):
    genre = Genre.query.all()
    track = Track.query.all()
    return render_template('views/edit.html', genre=genre, track=track)
    # return "page to edit a track. Task 2 complete!"

# Set route for deleteTrack function here
@main.route('/songbase/genre/<int:genre_id>/track/<int:track_id>/delete/')
def deleteTrack(genre_id, track_id):
    genre = Genre.query.all()
    track = Track.query.all()
    return render_template('views/delete.html', genre=genre, track=track)
    # return "page to delete a track. Task 3 complete!"
