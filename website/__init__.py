from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "blogapp.db"

def createapp():
    #configuring Flask modules
    myapp = Flask(__name__)
    myapp.config["SECRET_KEY"] = "key_jana"
    myapp.config['SECRET_KEY'] = "helloworld"

    #configuring SQL
    myapp.config['SQL_ALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(myapp)
    create_database(myapp)

    #importing blueprints
    from .views import views
    myapp.register_blueprint(views,url_prefix="/")

    from .auth import auth
    myapp.register_blueprint(auth,url_prefix="/")



    return myapp



def create_database(myapp):
    if not path.exists("website/"+DB_NAME):
        db.create_all(app=myapp)
        print("Database created!")