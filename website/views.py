from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user
#this particular file "views.py" is created to organise all types of view pages that the users sees
views = Blueprint("views", __name__)




@views.route('/')
@views.route('/home')
@login_required #only if there is a user logged in, he can access home page !
def home():
    return render_template('home.html')