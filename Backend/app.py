from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from Views import *

app = Flask(__name__)
db = SQLAlchemy()

app.config["JWT_SECRET_KEY"] = "super-secret"
app.config [" SQLALCHEMY_DATABASE_URI"] = "sqlite:///personal-journal.db"

db.init_app(app)
jwt = JWTManager(app)


