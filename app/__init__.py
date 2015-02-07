__author__ = 'Girish'
from flask import Flask

from config import config
from flask.ext.bootstrap import Bootstrap
bootstrap = Bootstrap()


def create_app(config_name):
    app=Flask(__name__)
    bootstrap.init_app(app)
    app.config.from_object(config[config_name])
    from app.talks import talks as talks_blueprint
    app.register_blueprint(talks_blueprint)
    return app


