from flask import Blueprint, render_template, redirect, url_for, request, flash
#this particular file "auth.py" is created to organise all types of authentication pages that the users sees
from . import db
from .dbmodels import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)

@auth.route('/login',methods=["GET","POST"])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password): #user.password is the hashed password.
                flash("Logged in!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template('login.html',user=current_user)


@auth.route('/signup',methods=["GET","POST"])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        email_exists = User.query.filter_by(email=email).first()#filter_by(column-name=VALUE)
        username_exists = User.query.filter_by(username=username).first()

        if email_exists:
            flash('Email is already in use.', category='error')
        elif username_exists:
            flash('Username is already in use.', category='error')
        elif password1 != password2:
            flash('Password don\'t match!', category='error')
        elif len(username) < 2:
            flash('Username is too short.', category='error')
        elif len(password1) < 6:
            flash('Password is too short.', category='error')
        elif len(email) < 4:
            flash("Email is invalid.", category='error')
        else:
            new_user = User(email = email, username = username, password = generate_password_hash(password1, method = 'sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User created!')
            return redirect(url_for('views.home'))
    return render_template('signup.html',user=current_user)


@auth.route('/logout')
@login_required #only if a user is logged in, he can logout. (login_req decorator checks the login_user func to look for any user that has logged in)
def logout():
    logout_user()
    return redirect(url_for('views.home'))
    ''' when the user presses logout, instead of a new logout.html template, we are redirecting him
    to the home page by accessing the home() function of 'views' BLUEPRINT. '''