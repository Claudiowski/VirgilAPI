# coding: utf-8

import datetime

from flask import g, request, Response, current_app
from flask_restful import Resource, marshal_with, abort, reqparse

from ..models import FavoriteDao, StreamDao, ReaderDao, CategoryDao, ThemeDao

from .parsers import favorite_fields

from datetime import datetime


class Favorite(Resource):
    """ Flask_restful Resource for Favorite entity, for routes with a parameter. """

    @marshal_with(favorite_fields)
    def get(self, id_fav):
        """ Returns a single Favorite. """

        session = current_app.session

        favorite = session.query(FavoriteDao).filter(FavoriteDao.id == id_fav).first()

        if favorite is None:
            return None, 204

        return favorite, 200

    def delete(self, id_fav):
        """ Deletes a single Favorite. """

        session = current_app.session

        if not session.query(FavoriteDao).filter(FavoriteDao.id == id_fav).delete():
            None, 204

        session.commit()
        return '', 200

    def put(self, id_fav):
        """ Edits a single Favorite. """

        session = current_app.session

        data = request.json
        favorite = session.query(FavoriteDao).filter(FavoriteDao.id == id_fav).first()

        if favorite is None:
            return None, 204

        favorite = format_update_favorite(favorite, data)
        session.commit()

        return '', 200


class FavoriteList(Resource):
    """ Flask_restful Resource for Favorite entity, for routes with no parameter."""

    @marshal_with(favorite_fields)
    def get(self, id_reader=None):
        """ Returns every single Favorite. """

        session = current_app.session

        if id_reader:
            favorites = session.query(FavoriteDao).join(StreamDao).join(CategoryDao)\
                            .join(ThemeDao).join(ReaderDao)\
                            .filter(ReaderDao.id == id_reader)\
                            .all()

        elif request.args.get('_categories'):
            args = reqparse.RequestParser().add_argument('_categories').parse_args()
            args = args['_categories'].split(',')
            favorites = session.query(FavoriteDao).join(StreamDao).join(CategoryDao)\
                    .filter(CategoryDao.id.in_(args))\
                    .all()

        elif request.args.get('_themes'):
            args = reqparse.RequestParser().add_argument('_themes').parse_args()
            args = args['_themes'].split(',')
            favorites = session.query(FavoriteDao).join(StreamDao).join(CategoryDao)\
                    .join(ThemeDao).filter(CategoryDao.id.in_(args))\
                    .all()

        else:
            favorites = session.query(FavoriteDao).all()

        if len(favorites) is 0:
            return None, 204

        return favorites, 200

    @marshal_with(favorite_fields)
    def post(self):
        """ Posts a single Favorite. """

        session = current_app.session

        data = request.json

        print(data)

        annotation = data.get('annotation')
        url = data.get('url')
        title = data.get('title')
        description = data.get('description')
        publication_date = data.get('publication_date')
        id_stream = data.get('id_stream')

        favorite = FavoriteDao(annotation=annotation, url=url, title=title, description=description,\
                               publication_date=publication_date, id_stream=id_stream)

        if favorite is None:
            return None, 202

        session.add(favorite)
        session.commit()
        return favorite, 200


def format_update_favorite(source_object, parameters):
    
    source_object.annotation = parameters.get('annotation')\
        if parameters.get('url') else source_object.url
    source_object.url = parameters.get('url')\
        if parameters.get('url') else source_object.url
    source_object.title = parameters.get('title')\
        if parameters.get('title') else source_object.title
    source_object.description = parameters.get('description')\
        if parameters.get('description') else source_object.description
    source_object.publication_date = datetime(parameters.get('publication_date'))\
        if parameters.get('publication_date') else source_object.publication_date
    source_object.id_stream = parameters.get('id_stream')\
        if parameters.get('id_stream') else source_object.id_stream

    return source_object