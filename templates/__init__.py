from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import login_manager




def createapp():
    myapp = Flask(__name__)
    myapp.config["SECRET_KEY"] = "key_jana"

    from .views import views
    myapp.register_blueprint(views,url_prefix="/")

    from .auth import auth
    myapp.register_blueprint(auth,url_prefix="/")



    return myapp