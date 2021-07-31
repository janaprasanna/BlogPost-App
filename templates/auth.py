from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route('/login')
def login():
    return "Login page"
@auth.route('/signup')
def signup():
    return "sign up page"