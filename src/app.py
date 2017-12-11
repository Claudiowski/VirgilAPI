# coding: utf8

""" Signalization board for the app. Every route is defined here. """

# frameworks
from flask import Flask, request
from flask_restful import Api, abort

import jwt

from sqlalchemy.ext.declarative import declarative_base

from Resources.Reader import *
from Resources.Theme import *
from Resources.Category import *
from Resources.Stream import *
from Resources.Favorite import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)

api = Api(app)


# Routes for readers
api.add_resource(ReaderList, '/readers')
api.add_resource(Reader, '/readers/<read_id>')

api.add_resource(ThemeList, '/themes')
api.add_resource(Theme, '/themes/<theme_id>')

api.add_resource(CategoryList, '/categories')
api.add_resource(Category, '/categories/<cat_id>')

api.add_resource(StreamList, '/streams')
api.add_resource(Stream, '/streams/<stream_id>')

api.add_resource(FavoriteList, '/favorites')
api.add_resource(Favorite, '/favorites/<favorite_id>')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
