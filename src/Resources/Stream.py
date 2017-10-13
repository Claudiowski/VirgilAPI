# coding: utf-8

from flask import g, request, Response, jsonify
from flask_restful import Resource, fields, marshal_with, abort

from DbAccess.Service import *
from Entities.StreamDao import *


def stream_queries():
    """ Gets an instance of  StreamQueries' from the 'g' environment. """
    if not hasattr(g, 'stream_queries'):
        g.stream_queries = StreamQueries()
    return g.stream_queries


class StreamQueries:
    """ Manager for Stream entity related SQL queries. """
    
    def select_query(self):
        """ Returns a 'SELECT' query for a single Stream. """
        return "SELECT * FROM stream WHERE id = %s"

    def delete_query(self):
        """ Returns a 'DELETE' query for a single Stream. """
        return "DELETE FROM stream WHERE id = %s"

    def select_all_query(self):
        """ Returns a 'SELECT' query for a single Stream. """
        return "SELECT * FROM stream"

    def insert_query(self):
        """ Returns an 'INSERT' query for a single Stream. """
        query = "INSERT INTO stream(url, name, id_category)"
        return query + " VALUES(%s, %s, %s) RETURNING *"

    def update_query(self, key_list):
        """ Returns an 'UPDATE' query for a single Stream. """
        temp = ""
        for k in range(len(key_list)):
            temp += key_list[k] + " = %s, "
        return "UPDATE stream SET " + temp[:-2] + " WHERE id = %s"


class Stream(Resource):
    """ Flask_restful Resource for Stream entity, for routes with a parameter. """

    @marshal_with(resource_fields)
    def get(self, stream_id):
        """ Returns a single Stream. """
        query = stream_queries().select_query()
        stream = get_service().get_content(query, [stream_id])
        if stream is None:
            abort(404, message="Stream {} does not exist.".format(stream_id))
        return StreamDao(stream), 200

    def delete(self, stream_id):
        """ Deletes a single Stream. """
        query = stream_queries().delete_query()
        value = get_service().del_content(query, [stream_id])
        if value != 1:
            abort(404, message="Stream {} does not exist.".format(stream_id))
        return '', 200

    def put(self, stream_id):
        """ Edits a single Stream. """
        key_list, value_list = [], []
        for key, value in request.form.items():
            key_list.append(key)
            value_list.append(value)
        value_list.append(stream_id)
        query = stream_queries().update_query(key_list)
        value = get_service().put_content(query, value_list)
        if value != 1:
            abort(400, message="The stream could not be updated.")
        return '', 200


class StreamList(Resource):
    """ Flask_restful Resource for Stream entity, for routes with no parameter."""

    @marshal_with(resource_fields)
    def get(self):
        """ Returns every single Stream. """
        query = stream_queries().select_all_query()
        streams = get_service().get_contents(query)
        if streams is None:
            abort(404, "No stream in database.")
        array_to_return = []
        for e in streams:
            array_to_return.append(StreamDao(e))
        return array_to_return, 200

    @marshal_with(resource_fields)
    def post(self):
        """ Posts a single Stream. """
        query = stream_queries().insert_query()
        name = request.form['name']
        url = request.form['url']
        id_cate = request.form['id_category']
        stream = get_service().post_content(query, [url, name, id_cate])
        if stream is None:
            return abort(400, "The stream could not be created.")
        return StreamDao(stream), 200
