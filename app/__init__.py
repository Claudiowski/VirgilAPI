# coding: utf-8

from flask import Flask, Blueprint
from flask_restful import Api

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .Resources import register_endpoints

from .ArticleRenewer import ArticleRenewer

from .config import config


def create_app(config_name='development'):
    
    app = Flask(__name__)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api = Api(blueprint)
    app.register_blueprint(blueprint)

    conf = config[config_name]
    app.config.from_object(conf)

    engine = create_engine(conf.DB_URI + conf.DB_USER + ':'\
             + conf.DB_PASSWORD + '@' + conf.DB_HOST + '/' + conf.DB_NAME)

    app.session = sessionmaker(bind=engine)()

    register_endpoints(api)

    ArticleRenewer(app.session).start()
    
    return app
