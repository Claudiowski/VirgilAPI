#coding: utf8

from flask import request
from flask_restful import Resource, abort, marshal_with, fields

from DbAccess.Service import *
from Entities.StreamDao import *
from Authentication.Authentication import *


class StreamByReader(Resource):
    """ Flask_restful Resource for Stream entity by Reader."""

    @marshal_with(resource_fields)
    def post(self):
        query = "SELECT * FROM stream s"
        query += " INNER JOIN category c ON s.id_category = c.id"
        query += " INNER JOIN theme t ON c.id = t.id_category"
        query += " WHERE t.id = %s"
        id_reader = request.form['id_reader']
        themebyread = get_service().get_custom_contents(query, [id_reader])
        if themebyread is None:
            abort(404, "No theme corresponding to this user in database.")
        array_to_return = []
        for e in themebyread:
            array_to_return.append(ThemeDao(e))
        return array_to_return, 200
