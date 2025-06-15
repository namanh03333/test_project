from flask import Flask
from flask_smorest import Api
from app.core.config import BaseConfig
from app.core.extensions import db, jwt, migrate
from app.api.api_user import blp as UserBlueprint
from app.api.auth import blp as AuthBlueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    api = Api(app)
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(AuthBlueprint)

    return app
