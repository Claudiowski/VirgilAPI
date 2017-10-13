from flask import request
from flask_restful import Resource, abort, marshal_with, fields

from DbAccess.Service import *
from Entities.StreamDao import *
from Authentication.Authentication import *


class CompleteStreamByReader(Resource):

    @marshal_with(resource_fields)
    def post(self):
        query = "SELECT s.id, s.url, s.name, s.id_category, c.name, t.id, t.name FROM stream s"
        query += " INNER JOIN category c ON s.id_category = c.id"
        query += " INNER JOIN theme t ON c.id_theme = t.id"
        query += " WHERE t.id_reader = %s"
        id_reader = request.form['id_reader']
        str_by_read = get_service().get_custom_contents(query, [id_reader])
        if str_by_read is None:
            abort(404, "No stream corresponding to this reader in database.")
        array_to_return = []
        for e in str_by_read:
            array_to_return.append(StreamDao(e))
        return array_to_return, 200