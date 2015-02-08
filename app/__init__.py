__author__ = 'Girish'
from flask import Flask

from config import config
from flask.ext.bootstrap import Bootstrap
bootstrap = Bootstrap()
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from .model import User

def create_app(config_name):
    app=Flask(__name__)
    bootstrap.init_app(app)
    db.init_app(app)
    app.config.from_object(config[config_name])
    from app.talks import talks as talks_blueprint
    app.register_blueprint(talks_blueprint)
    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/auth')
    print(app.url_map)
    return app


