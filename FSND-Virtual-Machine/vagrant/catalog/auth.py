from .models import User
from flask import Blueprint, render_template, redirect, url_for, \
    request, flash, jsonify
from werkzeug.security import generate_password_hash, \
    check_password_hash
from flask_login import login_user, logout_user, \
    login_required, current_user
from catalog import db


auth = Blueprint(
                'auth', __name__,
                template_folder='templates',
                static_folder='static'
)

# Authentications
@auth.route('/songbase/login')
def login():
    return render_template('auth/login.html')


@auth.route('/songbase/register')
def register():
    return render_template('auth/register.html')


@auth.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.register'))

    new_user = User(
        email=email, name=name,
        password=generate_password_hash(password,
                                        method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/songbase/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)

    return redirect(url_for('auth.profile'))


@auth.route('/songbase/profile')
@login_required
def profile():
    return render_template('auth/profile.html', name=current_user.name)


@auth.route('/songbase/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))
