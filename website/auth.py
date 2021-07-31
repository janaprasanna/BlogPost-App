from flask import Blueprint, render_template, redirect, url_for
#this particular file "auth.py" is created to organise all types of authentication pages that the users sees

auth = Blueprint("auth", __name__)

@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/signup')
def sign_up():
    return render_template('signup.html')


@auth.route('/logout')
def logout():
    return redirect(url_for('views.home'))
    ''' when the user presses logout, instead of a new logout.html template, we are redirecting him
    to the home page by accessing the home() function of 'views' BLUEPRINT. '''