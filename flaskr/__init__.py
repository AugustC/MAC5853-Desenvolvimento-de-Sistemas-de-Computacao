import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

db = SQLAlchemy()
api = Api()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'flaskr.mysql'),
            SQLALCHEMY_DATABASE_URI='mysql://db_admin:dbadmin@localhost/dsvdb'
            )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    db.init_app(app)
    from . import resources
    from . import dashboard
    api.init_app(app)
    from . import urlinput
    app.register_blueprint(urlinput.bp)
    app.register_blueprint(dashboard.bp)
    migrate = Migrate(app, db)
    from . import models
    return app
