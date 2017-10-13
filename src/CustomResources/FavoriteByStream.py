from flask import request
from flask_restful import Resource, abort, marshal_with, fields

from DbAccess.Service import *
from Entities.FavoriteDao import *


class FavoriteByStream(Resource):
    """ Flask_restful Resource for Favorite entity, for routes with no parameter."""

    @marshal_with(resource_fields)
    def post(self):
        query = "SELECT * FROM favorite WHERE id_stream = %s"
        id_category = request.form['id_stream']
        favbs = get_service().get_contents(query, [id_category])
        if favbs is None:
            abort(404, "No favorite corresponding to this stream in database.")
        array_to_return = []
        for e in favbs:
            array_to_return.append(FavoriteDao(e))
        return array_to_return, 200
