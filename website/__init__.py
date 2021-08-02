from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "blogapp.db"
#database name

def createapp():
    #configuring Flask modules
    myapp = Flask(__name__)
    myapp.config["SECRET_KEY"] = "key_jana"
    myapp.config['SECRET_KEY'] = "helloworld"

    #configuring SQL
    myapp.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #myapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(myapp)


    #importing blueprints
    from .views import views
    myapp.register_blueprint(views,url_prefix="/")

    from .auth import auth
    myapp.register_blueprint(auth,url_prefix="/")

    #NOTR: WITHOUT IMPORTING THE TABLES DO NOT CREATE THE DATABASE !!
    from .dbmodels import User
    create_database(myapp)
    #configuring login manager (controls the login and log out process
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    #if someone visits a page, and if they are not logged in, this particular function (login_view) redirects them to /login using auth blueprint
    login_manager.init_app(myapp)

    '''allows to access info of a user from the db given the ID. LoginManager uses a SESSION to store the ID and other small data of a user
     that is logged in. So when we want to access a particular info (say the  user's name, email etc) it uses this ID  '''
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return myapp



def create_database(myapp):
    #if the db is not found in the path,  it would create one.
    if not path.exists("website/"+DB_NAME):
        db.create_all(app=myapp)
        print("Database created!")