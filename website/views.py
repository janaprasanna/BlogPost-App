from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask_login import login_required, current_user
from sqlalchemy.sql.expression import text #current user method stores the info of recently logged in or currently logged in user in session
#this particular file "views.py" is created to organise all types of view pages that the users sees
views = Blueprint("views", __name__)
from . import db
from .dbmodels import Post, User, Comment




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


#a dyaamic route
@views.route('/delete-post/<id>')
@login_required
def del_post(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        flash("post doesnt exist." , category="error")
    elif current_user.id != post.id:
        flash("you do not have permission to delete this.", category="error")
        #if somebody directly tries to delete the post via http link eg: /delete-post/1
    else:
        db.session.delete(post)
        db.session.commit()
        flash("Post Deleted Successfully.")

    return redirect(url_for('views.home'))


@views.route('/posts/<username>')
@login_required
def viewmypost(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        flash("No user with that username exists.", category="error")
        return redirect(url_for('views.home'))
    post=user.posts #or
    #post = Post.query.filter_by(author=user.id).all()
    return render_template('posts.html',user=current_user, posts=post,username=username)


#adding comments to database
@views.route('/comment/<postid>',methods=["GET","POST"])
def create_comment(postid):
    if request.method == "POST":
        comment = request.form.get("text")
        if not comment:
            flash("Field is empty !!")
        else:
            post =  Post.query.filter_by(id=postid)
            if post:
                add_comment = Comment(text=comment, author=current_user.id, post_id=postid)
                db.session.add(add_comment)
                db.session.commit()
            else:
                flash("Post Doesnt Exists!!", category="error")
        return redirect(url_for('views.home'))
