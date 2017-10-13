from flask import request
from flask_restful import Resource, abort, marshal_with, fields

from DbAccess.Service import *
from Entities.CategoryDao import *


class CategoryByThemeName(Resource):
    """ Flask_restful Resource for Favorite entity, for routes with no parameter."""

    @marshal_with(resource_fields)
    def post(self):
        query = "SELECT c.name, c.id, c.id_theme, t.name FROM category c"
        query += " INNER JOIN theme t ON c.id_theme = t.id"
        query += " WHERE t.name = %s AND t.id_reader = %s"
        name_theme = request.form['name_theme']
        id_reader = request.form['id_reader']
        catbt = get_service().get_custom_contents(query, [name_theme, id_reader])
        if catbt is None:
            abort(404, "No category corresponding to this theme in database.")
        array_to_return = []
        for e in catbt:
            array_to_return.append(CategoryDao(e))
        return array_to_return, 200


class CategoryByThemeId(Resource):

    @marshal_with(resource_fields)
    def post(self):
        query = "SELECT c.id, c.name, c.id_theme, t.name FROM category c"
        query += " INNER JOIN theme t ON c.id_theme = t.id"
        query += " WHERE t.id = %s"
        id_theme = request.form['id_theme']
        array_to_return = []
        catbt = get_service().get_custom_contents(query, [id_theme])
        if catbt is None:
            abort(404, "No category corresponding to this theme in database.")
        for e in catbt:
            array_to_return.append(CategoryDao(e))
        return array_to_return, 200
