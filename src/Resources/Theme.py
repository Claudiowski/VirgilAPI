# coding: utf-8

from flask import g, request, Response, jsonify
from flask_restful import Resource, marshal_with, abort

from models import ThemeDao

from parsers import theme_fields

from utils import session

class Theme(Resource):
    """ Flask_restful Resource for Theme entity, for routes with a parameter. """

    @marshal_with(theme_fields)
    def get(self, theme_id):
        """ Returns a single Theme. """

        theme = session().query(ThemeDao).filter(ThemeDao.id == theme_id)

        if theme is None:
            abort(404, message="Theme {} does not exist.".format(theme_id))

        return ThemeDao(theme), 200

    def delete(self, theme_id):
        """ Deletes a single Theme. """

        if session().query(ThemeDao).filter(ThemeDao.id == theme_id).delete():
            abort(404, message="Theme {} does not exist.".format(theme_id))

        session().commit()
        return '', 200

    def put(self, theme_id):
        """ Edits a single Theme. """

        data = request.json
        theme = session().query(ThemeDao).filter(ThemeDao.id == theme_id)

        if theme is None():
            abort(404, message="Theme not found.")

        theme = format_update_theme(theme, data)
        session().commit()

        return '', 200


class ThemeList(Resource):
    """ Flask_restful Resource for Theme entity, for routes with no parameter."""

    @marshal_with(theme_fields)
    def get(self):
        """ Returns every single Theme. """

        themes = session().query(ThemeDao).all()

        if themes is None:
            abort(404, "No theme in database.")

        array_to_return = []
        
        for e in themes:
            array_to_return.append(ThemeDao(e))

        return array_to_return, 200

    @marshal_with(theme_fields)
    def post(self):
        """ Posts a single Theme. """

        data = request.json
        name = data.get('name')
        id_read = data.get('id_reader')

        theme = ThemeDao(name, id_read)

        theme = session().add(theme)

        if theme is None:
            return abort(400, "The theme could not be created.")

        session.commit()
        return theme, 200


def format_update_theme(source_object, parameters):
    
    body = {}

    theme.name = parameters.get('name')\
        if parameters.get('name') else source_object.name
    theme.id_reader = parameters.get('id_reader')\
        if parameters.get('id_reader') else source_object.id_reader

    return body