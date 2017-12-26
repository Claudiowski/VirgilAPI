# coding: utf-8

from flask import g, request, Response, current_app
from flask_restful import Resource, marshal_with, abort

from ..models import ThemeDao

from .parsers import theme_fields


class Theme(Resource):
    """ Flask_restful Resource for Theme entity, for routes with a parameter. """

    @marshal_with(theme_fields)
    def get(self, id_theme):
        """ Returns a single Theme. """

        session = current_app.session

        theme = session.query(ThemeDao).filter(ThemeDao.id == id_theme).first()

        if theme is None:
            return None, 204

        return theme, 200

    def delete(self, id_theme):
        """ Deletes a single Theme. """

        session = current_app.session

        if not session.query(ThemeDao).filter(ThemeDao.id == id_theme).delete():
            return None, 204

        session.commit()
        return '', 200

    def put(self, id_theme):
        """ Edits a single Theme. """

        session = current_app.session

        data = request.json
        theme = session.query(ThemeDao).filter(ThemeDao.id == id_theme).first()

        if theme is None:
            return None, 204

        theme = format_update_theme(theme, data)
        session.commit()

        return '', 200


class ThemeList(Resource):
    """ Flask_restful Resource for Theme entity, for routes with no parameter."""

    @marshal_with(theme_fields)
    def get(self, id_reader=None):
        """ Returns every single Theme. """

        session = current_app.session

        args = request.args

        if id_reader:
            themes = session.query(ThemeDao).filter(ThemeDao.id_reader == id_reader).all()
        else:
            themes = session.query(ThemeDao).all()

        if len(themes) is 0:
            return None, 204

        return themes, 200

    @marshal_with(theme_fields)
    def post(self):
        """ Posts a single Theme. """

        session = current_app.session

        data = request.json
        name = data.get('name')
        id_read = data.get('id_reader')

        theme = ThemeDao(name=name, id_reader=id_read)

        if theme is None:
            return None, 202

        session.add(theme)
        session.commit()
        return theme, 200


def format_update_theme(source_object, parameters):
    
    source_object.name = parameters.get('name')\
        if parameters.get('name') else source_object.name
    source_object.id_reader = parameters.get('id_reader')\
        if parameters.get('id_reader') else source_object.id_reader

    return source_object