from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# '.' refers current folder
#model means tables generally


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    comments = db.relationship('Comment', backref='user', passive_deletes=True)
    #from User table we have to access Post by using Relationship
    posts = db.relationship('Post', backref='user', passive_deletes=True)
    '''this column is going to reference all the posts that this user has. 
    1 user - N posts relationship '''
    '''backref - backreference
    from the Post table, we can access the User object that created the Post (. operator)
    instead of using "author" var to access, we can use post.obj to access.
    eg:
    p= Post (..)
    >> p.id = int(id)'''


#A Table to store all the posts of each user
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

    comments = db.relationship('Comment', backref='post', passive_deletes=True)
    #from POst table we are acesssing user.
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    '''author field stores the ID of an user who created this post.
     A user who is making a post should by existing.'''

    '''user.id where user represents the table name, by default in sql, tables names
    are always in lowercase. ondelete property states that when we delete a user from the 
    table, this property automatically cascades and deletes all the posts made by him'''





class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete="CASCADE"), nullable=False)
