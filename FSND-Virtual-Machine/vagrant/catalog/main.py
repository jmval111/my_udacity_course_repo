#! /usr/bin/python3
from .models import Genre, Track
from flask import Blueprint, render_template,\
    redirect, url_for, request, jsonify
from sqlalchemy import desc, func
from . import quesession


main = Blueprint(
                'main', __name__,
                template_folder='templates',
                static_folder='static'
)

# Views
@main.route("/")
@main.route("/songbase/")
def home():
    genre = quesession.query(Genre).\
        order_by(desc(Genre.name))
    quesession.close()
    track = quesession.query(Track).\
        order_by(desc(Track.date)).limit(5)
    quesession.close()
    return render_template(
        'views/home.html',
        genre=genre,
        track=track
    )

# Show all tracks availiable within selected Genre <genre.name>/
@main.route('/songbase/<path:genre_name>/<int:genre_id>')
def showTracks(genre_name, genre_id):
    gen_title = Genre.query.\
        filter(Genre.id == genre_id)
    track = Track.query.\
        filter(Track.gen_id == genre_id).\
        order_by(desc(Track.date)).all()
    trk_count = quesession.query(func.count(Track.id)).\
        filter(Track.gen_id == genre_id)
    quesession.close()
    full = quesession.query(Genre.name, Track.name, Track.slug, Track.id).\
        filter(Genre.id == genre_id, Track.gen_id == genre_id).all()
    quesession.close()
    return render_template(
        'views/tracks.html',
        gen_title=gen_title,
        track=track,
        trk_count=trk_count,
        full=full
    )

# Show selected track infromation <genre_name>/<track_name>/
@main.route('/songbase/<path:genre_name>/<path:track_name>/<int:track_id>')
def trackInfo(genre_name, track_name, track_id):
    genre = Genre.query.\
        filter(Genre.name == genre_name)
    track = quesession.query(Track.name).\
        filter(Track.slug == track_name)
    quesession.close()
    full = quesession.query(Track.description).\
        filter(Track.id == track_id)
    quesession.close()
    return render_template(
        'views/info.html',
        genre=genre,
        track=track,
        full=full
    )


@main.route('/songbase/add-genre')
def addGenre():
    genre = Genre.query.all()
    track = Track.query.all()
    return render_template(
        'views/add-genre.html',
        genre=genre,
        track=track
    )
    # return "page to add a track. Task 1 complete!"

# Set route for addTrack function here
@main.route('/songbase/add-track')
def addTrack():
    genre = Genre.query.all()
    track = Track.query.all()
    return render_template(
        'views/add-track.html',
        genre=genre,
        track=track
    )
    # return "page to add a track. Task 1 complete!"

# Set route for editTrack function here
@main.route('/songbase/genre/<int:genre_id>/track/<int:track_id>/edit/')
def editTrack(genre_id, track_id):
    genre = Genre.query.all()
    track = Track.query.all()
    return render_template(
        'views/edit.html',
        genre=genre,
        track=track
    )
    # return "page to edit a track. Task 2 complete!"

# Set route for deleteTrack function here
@main.route('/songbase/genre/<int:genre_id>/track/<int:track_id>/delete/')
def deleteTrack(genre_id, track_id):
    genre = Genre.query.all()
    track = Track.query.all()
    return render_template(
        'views/delete.html',
        genre=genre,
        track=track
    )
    # return "page to delete a track. Task 3 complete!"
