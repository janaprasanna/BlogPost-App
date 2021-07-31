from flask import Blueprint, render_template
#this particular file "views.py" is created to organise all types of view pages that the users sees
views = Blueprint("views", __name__)




@views.route('/')
def home():
    return "HOME"