from flask import Blueprint, render_template
#this particular file "auth.py" is created to organise all types of authentication pages that the users sees

auth = Blueprint("auth", __name__)

@auth.route('/login')
def login():
    return "Login page"
@auth.route('/signup')
def signup():
    return "sign up page"