from flask import Blueprint, render_template, url_for
#this particular file "views.py" is created to organise all types of view pages that the users sees
views = Blueprint("views", __name__)




@views.route('/')
@views.route('/home')
def home():
    return render_template('home.html')