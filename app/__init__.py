from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .views.home import home_blueprint
    app.register_blueprint(home_blueprint)

    from .views.autoExam import autoExam_blueprint
    app.register_blueprint(autoExam_blueprint)

    return app
