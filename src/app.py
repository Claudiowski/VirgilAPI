# coding: utf8

""" Signalization board for the app. Every route is defined here. """

# frameworks
from flask import Flask, request
from flask_restful import Api, abort

import jwt

from sqlalchemy.ext.declarative import declarative_base

# local imports
from Authentication.Token import *

from Resources.Reader import *
from Resources.Theme import *
from Resources.Category import *
from Resources.Stream import *
from Resources.Favorite import *

from CustomResources.CategoryByTheme import *
from CustomResources.StreamByCategory import *
from CustomResources.FavoriteByStream import *
from CustomResources.StreamByTheme import *
from CustomResources.CompleteStreamByReader import *

from CustomResources.ThemeByReader import *
from CustomResources.FavoriteByReader import *
from CustomResources.CategoryByReader import *
from CustomResources.StreamByReader import *

from CustomResources.FavoriteByCategory import *
from CustomResources.FavoriteByTheme import *


app = Flask(__name__)

api = Api(app)

g.Base = declarative_base()


# Route for authentication
api.add_resource(Token, '/auth/token')

# Routes for readers
api.add_resource(ReaderList, '/readers')
api.add_resource(Reader, '/readers/<read_id>')

# Routes for themes
api.add_resource(ThemeList, '/themes')
api.add_resource(Theme, '/themes/<theme_id>')

# Routes for categories
api.add_resource(CategoryList, '/categories')
api.add_resource(Category, '/categories/<cat_id>')

# Routes for streams
api.add_resource(StreamList, '/streams')
api.add_resource(Stream, '/streams/<stream_id>')

# Routes for favorites
api.add_resource(FavoriteList, '/favorites')
api.add_resource(Favorite, '/favorites/<favorite_id>')

# Custom routes
api.add_resource(CategoryByThemeName, '/category-by-theme-name')
api.add_resource(CategoryByThemeId, '/category-by-theme-id')
api.add_resource(StreamByCategory, '/stream-by-category')
api.add_resource(FavoriteByStream, '/favorite-by-stream')

    # By category
api.add_resource(StreamByCategoryList, '/stream-by-category-list')
api.add_resource(FavoriteByCategoryList, '/favorite-by-category-list')

    # By theme
api.add_resource(StreamByThemeName, '/stream-by-theme-name')
api.add_resource(StreamByThemeId, '/stream-by-theme-id')
api.add_resource(StreamByThemeList, '/stream-by-theme-list')
api.add_resource(FavoriteByThemeList, '/favorite-by-theme-list')

    # By reader
api.add_resource(ThemeByReader, '/theme-by-reader')
api.add_resource(CompleteStreamByReader, '/complete-stream-by-reader')
api.add_resource(FavoriteByReader, '/favorite-by-reader')
api.add_resource(CategoryByReader, '/category-by-reader')
api.add_resource(StreamByReader, '/stream-by-reader')


@app.route('/auth/verification')
def auth_verification():
    try:
        token, reader_id, secret = get_auth_data()
        jwt.decode(token, secret)
        return '', 200
    except:
        abort(401, message="Invalid authentication.")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
