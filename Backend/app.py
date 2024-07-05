from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from extentions import db,jwt,migrate
from Views import *
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app,db)

    # register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)