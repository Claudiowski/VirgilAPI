# coding: utf-8

import datetime

from flask import g, request, Response, jsonify
from flask_restful import Resource, marshal_with, abort

from models import ThemeDao

from parsers import favorite_fields

from utils import session


class Favorite(Resource):
    """ Flask_restful Resource for Favorite entity, for routes with a parameter. """

    @marshal_with(favorite_fields)
    def get(self, favorite_id):
        """ Returns a single Favorite. """

        theme = session().query(ThemeDao).filter(ThemeDao.id == theme_id)

        if theme is None:
            abort(404, message="Theme {} does not exist.".format(theme_id))

        return ThemeDao(theme), 200

    def delete(self, favorite_id):
        """ Deletes a single Favorite. """

        if session().query(FavoriteDao).filter(FavoriteDao.id == favorite_id).delete():
            abort(404, message="Favorite {} does not exist.".format(favorite_id))

        session().commit()
        return '', 200

    def put(self, favorite_id):
        """ Edits a single Favorite. """

        data = request.json
        favorite = session().query(FavoriteDao).filter(FavoriteDao.id == favorite_id)

        if favorite is None():
            abort(404, message="Favorite not found.")

        favorite = format_update_favorite(favorite, data)
        session().commit()

        return '', 200


class FavoriteList(Resource):
    """ Flask_restful Resource for Favorite entity, for routes with no parameter."""

    @marshal_with(favorite_fields)
    def get(self):
        """ Returns every single Favorite. """

        favorites = session().query(FavoriteDao).all()

        if favorites is None:
            abort(404, "No favorite in database.")

        array_to_return = []
        
        for e in favorites:
            array_to_return.append(FavoriteDao(e))

        return array_to_return, 200

    @marshal_with(favorite_fields)
    def post(self):
        """ Posts a single Favorite. """

        data = request.json
        annotation = data.get('annotation')
        url = data.get('url')
        title = data.get('title')
        description = data.get('description')
        publication_date = data.get('publication_date')
        id_stream = data.get('id_stream')

        favorite = FavoriteDao(annotation, url, title, description, publication_date, id_stream)

        session().add(favorite)

        if favorite is None:
            return abort(400, "The favorite could not be created.")

        session.commit()
        return favorite, 200

def format_update_favorite(source_object, parameters):
    
    body = {}

    favorite.annotation = parameters.get('annotation')\
        if parameters.get('url') else source_object.url
    favorite.url = parameters.get('url')\
        if parameters.get('url') else source_object.url
    favorite.title = parameters.get('title')\
        if parameters.get('title') else source_object.title
    favorite.description = parameters.get('description')\
        if parameters.get('description') else source_object.description
    favorite.publication_date = parameters.get('publication_date')\
        if parameters.get('publication_date') else source_object.publication_date
    favorite.id_stream = parameters.get('id_stream')\
        if parameters.get('id_stream') else source_object.id_stream

    return body