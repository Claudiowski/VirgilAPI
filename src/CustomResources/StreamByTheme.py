from flask import request
from flask_restful import Resource, abort, marshal_with, fields

from DbAccess.Service import *
from Entities.StreamDao import *
from Authentication.Authentication import *


class StreamByThemeName(Resource):

    @marshal_with(resource_fields)
    def post(self):
        query = "SELECT s.id, s.url, s.name, s.id_category FROM stream s"
        query += " INNER JOIN category c ON s.id_category = c.id"
        query += " INNER JOIN theme t ON c.id_theme = t.id"
        query += " WHERE t.name = %s AND t.id_reader = %s"
        name_theme = request.form['name_theme']
        id_reader = request.form['id_reader']
        strbt = get_service().get_custom_contents(query, [name_theme, id_reader])
        if strbt is None:
            abort(404, "No stream corresponding to this theme in database.")
        array_to_return = []
        for e in strbt:
            array_to_return.append(StreamDao(e))
        return array_to_return, 200


class StreamByThemeId(Resource):

    @marshal_with(resource_fields)
    def post(self):
        query = "SELECT s.id, s.url, s.name, s.id_category FROM stream s"
        query += " INNER JOIN category c ON s.id_category = c.id"
        query += " WHERE c.id_theme = %s"
        id_theme = request.form['id_theme']
        strbt = get_service().get_custom_contents(query, [id_theme])
        if strbt is None:
            abort(404, "No stream corresponding to this theme in database.")
        array_to_return = []
        for e in strbt:
            array_to_return.append(StreamDao(e))
        return array_to_return, 200
