from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#import os
from application import config
from flask_cors import CORS
#from application.models import db
from application.views.game import bp_game


def intial_app(config_name='development'):

    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    app.config.from_object(config.config_setting[config_name])  # object-based default configuration
    app.config.from_pyfile('flask.cfg', silent=True)  # instance-folders configuration

    #db.init_app(app)
    app.register_blueprint(bp_game, url_prefix='/game')

    # with app.app_context():
    #     # db.drop_all()
    #     db.create_all()

    return app


