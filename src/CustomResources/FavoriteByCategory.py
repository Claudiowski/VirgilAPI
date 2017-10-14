from flask import request
from flask_restful import Resource, abort, marshal_with, fields

from DbAccess.Service import *
from Entities.FavoriteDao import *


class FavoriteByCategoryList(Resource):

    @marshal_with(resource_fields)
    def post(self):
        query = "SELECT f.id, f.url, f.annotation, f.title, f.description, f.date_hour, f.id_stream FROM favorite f"
        query += " INNER JOIN stream s ON s.id = f.id_stream"
        query += " WHERE s.id_category IN ("
        id_dict = request.json['id_categories']
        id_categories = []
        for e in id_dict: 
            query += "%s, "
            id_categories.append(int(e))
        favbc = get_service().get_custom_contents(query[:-2] + ")", id_categories)
        if favbc is None:
            abort(404, "No favorite corresponding to this category in database.")
        array_to_return = []
        for e in favbc:
            array_to_return.append(FavoriteDao(e))
        return array_to_return, 200