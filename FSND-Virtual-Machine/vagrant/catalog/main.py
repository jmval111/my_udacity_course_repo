#! /usr/bin/python3
from models import Genre, Track  # , User
from flask import Blueprint, flash, render_template, \
    redirect, url_for, request, abort  # , jsonify
from sqlalchemy import desc, func
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
from flask_login import login_required, current_user
from app import db, quesession


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


@main.route('/songbase/edit/genre')
def addGenre():
    genre = Genre.query.all()
    track = Track.query.all()
    return render_template(
        'views/edit-genre.html',
        genre=genre,
        track=track
    )


@main.route('/genre', methods=['POST'])
@login_required
def addGenre_post():
    name = request.form.get('name')

    genre = Genre.query.filter_by(name=name).first()

    if genre:
        flash('Genre already exists')
        return redirect(url_for('main.addGenre'))

    new_genre = Genre(name=name)

    db.session.add(new_genre)
    db.session.commit()

    return redirect(url_for('main.home'))


@main.route('/delete', methods=['POST'])
@login_required
def delete_genre():

    id = request.form.get('genres')

    genre = Genre.query.filter_by(id=id).first()
    # return(str(genre))
    if genre:
        db.session.delete(genre)
        db.session.commit()
        flash('Genre deleted!', 'success')

    return redirect(url_for('main.home'))
    # return "page to add a track. Task 1 complete!"

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

# Set route for addTrack function here
@main.route('/songbase/add/track')
@login_required
def addTrack():
    genre = Genre.query.all()
    track = Track.query.all()

    return render_template(
        'views/add-track.html',
        genre=genre,
        track=track
    )
    # return "page to add a track. Task 1 complete!"


@main.route('/track', methods=['POST'])
@login_required
def addTrack_post():
    name = request.form.get('name')
    slug = request.form.get('slug')
    gen_id = request.form.get('gen_id')
    description = request.form.get('description')

    track = Genre.query.filter_by(name=name).first()

    if track:
        flash('Track already exists')
        return redirect(url_for('main.addTrack'))

    new_track = Track(
        name=name,
        slug=slug,
        description=description,
        gen_id=gen_id
    )

    db.session.add(new_track)
    db.session.commit()
    flash('Genre deleted!', 'success')
    return redirect(url_for('main.home'))

# Show selected track infromation <genre_name>/<track_name>/
@main.route('/songbase/<path:genre_name>/<path:track_name>/<int:track_id>')
def trackInfo(genre_name, track_name, track_id):
    genre = Genre.query.\
        filter(Genre.name == genre_name)
    track = quesession.query(Track.name, Track.id, Track.slug).\
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

# Set route for editTrack function here
@main.route('/songbase/track/<path:track_slug>/<int:track_id>/edit/')
@login_required
def editTrack(track_slug, track_id):
    genre = Genre.query.all()
    track = Track.query.\
        filter(Track.id == track_id)
    return render_template(
        'views/edit-track.html',
        genre=genre,
        track=track
    )
    # return "page to edit a track. Task 2 complete!"

# Set route for editTrack function here
@main.route('/songbase/track/update/', methods=['GET', 'POST'])
@login_required
def editTrack_update(track_id):
    track = Track.query.\
        filter(Track.id == track_id).first()

    if track:
        name = request.form.get('name')
        slug = request.form.get('slug')
        gen_id = request.form.get('gen_id')
        description = request.form.get('description')

        track.name = name
        track.slug = slug
        track.gen_id = gen_id
        track.description = description

        db.session.commit()
        flash('Track has been updated!', 'success')

    return redirect(url_for('main.trackInfo', track_id=track.id))

# Set route for deleteTrack function here
@main.route('/track/<int:track_id>/delete', methods=['POST'])
@login_required
def deleteTrack(track_id):
    track = Track.query.get_or_404(track_id)
    db.session.delete(track)
    db.session.commit()
    flash('Track deleted!', 'success')
    return redirect(url_for('main.home'))
    # return "page to add a track. Task 1 complete!"
