from flask import Flask

from app.config import Config
from app.models import db


def create_app(config_object=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_object)

    db.init_app(app)

    from app.routes.urls import bp as urls_bp
    app.register_blueprint(urls_bp)

    with app.app_context():
        db.create_all()

    return app