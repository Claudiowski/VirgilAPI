from flask import request
from flask_restful import Resource, abort, marshal_with, fields

from DbAccess.Service import *
from Entities.StreamDao import *


class StreamByCategory(Resource):
    """ Flask_restful Resource for Favorite entity, for routes with no parameter."""

    @marshal_with(resource_fields)
    def post(self):
        query = "SELECT * FROM stream WHERE id_category = %s"
        id_category = request.form['id_category']
        strbc = get_service().get_contents(query, [id_category])
        if strbc is None:
            abort(404, "No stream corresponding to this category in database.")
        array_to_return = []
        for e in strbc:
            array_to_return.append(StreamDao(e))
        return array_to_return, 200
