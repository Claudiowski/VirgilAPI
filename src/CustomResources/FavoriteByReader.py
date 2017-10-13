from flask import request
from flask_restful import Resource, abort, marshal_with, fields

from DbAccess.Service import *
from Entities.FavoriteDao import *


class FavoriteByReader(Resource):
    """ Flask_restful Resource for Favorite entity, for routes with no parameter."""

    @marshal_with(resource_fields)
    def post(self):
        query = "SELECT f.url, f.annotation, f.id, f.id_stream, f.title, f.description, f.date_hour FROM favorite f"
        query += " INNER JOIN stream s ON f.id_stream = s.id"
        query += " INNER JOIN category c ON s.id_category = c.id"
        query += " INNER JOIN theme t ON c.id_theme = t.id"
        query += " INNER JOIN reader r ON t.id_reader = r.id"
        id_reader = request.form['id_reader']
        favbyread = get_service().get_custom_contents(query, [id_reader])
        if favbyread is None:
            abort(404, "No favorite corresponding to this reader in database.")
        array_to_return = []
        for e in favbyread:
            array_to_return.append(FavoriteDao(e))
        return array_to_return, 200
