import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt import JWT


from myapp.secure_check import authenticate,identity


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

######COnfiguring our app with db

app.config['SECRET_KEY'] = "mysecreto"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

####Configuring JWT with apur flask app
JWT(app,authenticate,identity)




