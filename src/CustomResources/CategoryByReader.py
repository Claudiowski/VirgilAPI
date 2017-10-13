from flask import request
from flask_restful import Resource, abort, marshal_with, fields

from DbAccess.Service import *
from Entities.CategoryDao import *


class CategoryByReader(Resource):

    @marshal_with(resource_fields)
    def post(self):
        query = "SELECT c.name, c.id, c.id_theme, t.name FROM category c"
        query += " INNER JOIN theme t ON c.id_theme = t.id"
        query += " WHERE t.id_reader = %s"
        id_reader = request.form['id_reader']
        catbyread = get_service().get_custom_contents(query, [id_reader])
        print(catbyread)
        if catbyread is None:
            abort(404, "No category corresponding to this reader in database.")
        array_to_return = []
        for e in catbyread:
            array_to_return.append(CategoryDao(e))
        return array_to_return, 200
