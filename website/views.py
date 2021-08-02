from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask_login import login_required, current_user #current user method stores the info of recently logged in or currently logged in user in session
#this particular file "views.py" is created to organise all types of view pages that the users sees
views = Blueprint("views", __name__)
from . import db
from .dbmodels import Post




@views.route('/')
@views.route('/home')
@login_required #only if there is a user logged in, he can access home page !
def home():
    posts = Post.query.all()
    return render_template('home.html',user=current_user,posts=posts)



@views.route('/create-post',methods=["GET","POST"])
@login_required
def create_post():
    if request.method == "POST":
        text = request.form.get("text")

        if not text:
            flash("Post cannot be empty !", category="error")
        else:
            #adding fresh post to db.
            post = Post(text=text,author=current_user.id)
            #id column and date column is auto filled.
            db.session.add(post)
            db.session.commit()
            flash("Post created :)", category="success")
            return  redirect(url_for('views.home'))
    return render_template('create_post.html',user=current_user)
