#coding: utf8

from flask import request
from flask_restful import Resource, abort, marshal_with, fields

from DbAccess.Service import *
from Entities.ThemeDao import *
from Authentication.Authentication import *


class ThemeByReader(Resource):
    """ Flask_restful Resource for Favorite entity, for routes with no parameter."""

    @marshal_with(resource_fields)
    def post(self):
        query = "SELECT * FROM theme WHERE id_reader = %s"
        id_reader = request.form['id_reader']
        themesbr = get_service().get_custom_contents(query, [id_reader])
        if themesbr is None:
            abort(404, "No theme corresponding to this user in database.")
        array_to_return = []
        for e in themesbr:
            array_to_return.append(ThemeDao(e))
        return array_to_return, 200
