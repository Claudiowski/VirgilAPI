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


class StreamByCategoryList(Resource):

    @marshal_with(resource_fields)
    def post(self):
        query = "SELECT s.id, s.url, s.name, s.id_category FROM stream s"
        query += " WHERE s.id_category IN ("
        id_dict = request.json['id_categories']
        id_categories = []
        for e in id_dict: 
            query += "%s, "
            id_categories.append(int(e))
        strbc = get_service().get_custom_contents(query[:-2] + ")", id_categories)
        if strbc is None:
            abort(404, "No stream corresponding to this category in database.")
        array_to_return = []
        for e in strbc:
            array_to_return.append(StreamDao(e))
        return array_to_return, 200
