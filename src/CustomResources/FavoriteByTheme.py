from flask import request
from flask_restful import Resource, abort, marshal_with, fields

from DbAccess.Service import *
from Entities.FavoriteDao import *


class FavoriteByThemeList(Resource):

    @marshal_with(resource_fields)
    def post(self):
        query = "SELECT f.id, f.url, f.annotation, f.title, f.description, f.date_hour, f.id_stream FROM favorite f"
        query += " INNER JOIN stream s ON s.id = f.id_stream"
        query += " INNER JOIN category c ON c.id = s.id_category"
        query += " WHERE c.id_theme IN ("
        id_dict = request.json['id_themes']
        id_themes = []
        for e in id_dict: 
            query += "%s, "
            id_themes.append(int(e))
        favbt = get_service().get_custom_contents(query[:-2] + ")", id_themes)
        if favbt is None:
            abort(404, "No favorite corresponding to this theme in database.")
        array_to_return = []
        for e in favbt:
            array_to_return.append(FavoriteDao(e))
        return array_to_return, 200