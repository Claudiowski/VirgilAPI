# coding: utf-8

from flask import g, request, Response, jsonify
from flask_restful import Resource, fields, marshal_with, abort

from DbAccess.Service import *
from Entities.ReaderDao import *


def reader_queries():
    """ Gets an instance of  ReaderQueries' from the 'g' environment. """
    if not hasattr(g, 'read_queries'):
        g.read_queries = ReaderQueries()
    return g.read_queries


class ReaderQueries:
    """ Manager for Reader entity related SQL queries. """
    
    def select_query(self):
        """ Returns a 'SELECT' query for a single Reader. """
        return "SELECT * FROM reader WHERE id = %s"

    def delete_query(self):
        """ Returns a 'DELETE' query for a single Reader. """
        return "DELETE FROM reader WHERE id = %s"

    def select_all_query(self):
        """ Returns a 'SELECT' query for a single Reader. """
        return "SELECT * FROM reader"

    def insert_query(self):
        """ Returns an 'INSERT' query for a single Reader. """
        query = "INSERT INTO reader(pseudo, password, secret)"
        return query + " VALUES(%s, %s, %s) RETURNING *"

    def update_query(self, key_list):
        """ Returns an 'UPDATE' query for a single Reader. """
        temp = ""
        for k in range(len(key_list)):
            temp += key_list[k] + " = %s, "
        return "UPDATE reader SET " + temp[:-2] + " WHERE id = %s"


class Reader(Resource):
    """ Flask_restful Resource for Reader entity, for routes with a parameter. """

    @marshal_with(resource_fields)
    def get(self, read_id):
        """ Returns a single Reader. """
        query = reader_queries().select_query()
        reader = get_service().get_content(query, [read_id])
        if reader is None:
            abort(404, message="Reader {} does not exist.".format(read_id))
        return ReaderDao(reader), 200

    def delete(self, read_id):
        """ Deletes a single Reader. """
        query = reader_queries().delete_query()
        value = get_service().del_content(query, [read_id])
        if value != 1:
            abort(404, message="Reader {} does not exist.".format(read_id))
        return '', 200

    def put(self, read_id):
        """ Edits a single Reader. """
        key_list, value_list = [], []
        for key, value in request.form.items():
            key_list.append(key)
            value_list.append(value)
        value_list.append(read_id)
        query = reader_queries().update_query(key_list)
        value = get_service().put_content(query, value_list)
        if value != 1:
            abort(400, message="The reader could not be updated.")
        return '', 200


class ReaderList(Resource):
    """ Flask_restful Resource for Reader entity, for routes with no parameter."""

    @marshal_with(resource_fields)
    def get(self):
        """ Returns every single Reader. """
        query = reader_queries().select_all_query()
        readers = get_service().get_contents(query)
        if readers is None:
            abort(404, "No reader in database.")
        array_to_return = []
        for e in readers:
            array_to_return.append(ReaderDao(e))
        return array_to_return, 200

    @marshal_with(resource_fields)
    def post(self):
        """ Posts a single Reader. """
        query = reader_queries().insert_query()
        pseudo = request.form['pseudo']
        pwd = request.form['password']
        secret = request.form['secret']
        reader = get_service().post_content(query, [pseudo, pwd, secret])
        if reader is None:
            return abort(400, "The reader could not be created.")
        return ReaderDao(reader), 200
