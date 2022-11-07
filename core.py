from flask import Flask, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from settings import *

#init + configure app, add session & sqlalchemy, stuff you basically likely won't change
#personal note: sqlalchemy is great
database = SQLAlchemy()
app = Flask("memeland-server")
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['ROOT_URL'] = ROOT_URL
Session(app)
database.init_app(app)
migrate = Migrate(app, database)
migrate.init_app(app, database)

@app.route("/")
def hello_world():
    session["name"] = "john"
    return "<p>konichiwa we are memeland</p>"