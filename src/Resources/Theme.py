# coding: utf-8

from flask import g, request, Response, jsonify
from flask_restful import Resource, fields, marshal_with, abort

from DbAccess.Service import *
from Entities.ThemeDao import *


def theme_queries():
    """ Gets an instance of  ThemeQueries' from the 'g' environment. """
    if not hasattr(g, 'theme_queries'):
        g.theme_queries = ThemeQueries()
    return g.theme_queries


class ThemeQueries:
    """ Manager for Theme entity related SQL queries. """
    
    def select_query(self):
        """ Returns a 'SELECT' query for a single Theme. """
        return "SELECT * FROM theme WHERE id = %s"

    def delete_query(self):
        """ Returns a 'DELETE' query for a single Theme. """
        return "DELETE FROM theme WHERE id = %s"

    def select_all_query(self):
        """ Returns a 'SELECT' query for a single Theme. """
        return "SELECT * FROM theme"

    def insert_query(self):
        """ Returns an 'INSERT' query for a single Theme. """
        query = "INSERT INTO theme(name, id_reader)"
        return query + " VALUES(%s, %s) RETURNING *"

    def update_query(self, key_list):
        """ Returns an 'UPDATE' query for a single Theme. """
        temp = ""
        for k in range(len(key_list)):
            temp += key_list[k] + " = %s, "
        return "UPDATE theme SET " + temp[:-2] + " WHERE id = %s"


class Theme(Resource):
    """ Flask_restful Resource for Theme entity, for routes with a parameter. """

    @marshal_with(resource_fields)
    def get(self, theme_id):
        """ Returns a single Theme. """
        query = theme_queries().select_query()
        theme = get_service().get_content(query, [theme_id])
        if theme is None:
            abort(404, message="Theme {} does not exist.".format(theme_id))
        return ThemeDao(theme), 200

    def delete(self, theme_id):
        """ Deletes a single Theme. """
        query = theme_queries().delete_query()
        value = get_service().del_content(query, [theme_id])
        if value != 1:
            abort(404, message="Theme {} does not exist.".format(theme_id))
        return '', 200

    def put(self, theme_id):
        """ Edits a single Theme. """
        key_list, value_list = [], []
        for key, value in request.form.items():
            key_list.append(key)
            value_list.append(value)
        value_list.append(theme_id)
        query = theme_queries().update_query(key_list)
        value = get_service().put_content(query, value_list)
        if value != 1:
            abort(400, message="The theme could not be updated.")
        return '', 200


class ThemeList(Resource):
    """ Flask_restful Resource for Theme entity, for routes with no parameter."""

    @marshal_with(resource_fields)
    def get(self):
        """ Returns every single Theme. """
        query = theme_queries().select_all_query()
        categories = get_service().get_contents(query)
        if categories is None:
            abort(404, "No theme in database.")
        array_to_return = []
        for e in categories:
            array_to_return.append(ThemeDao(e))
        return array_to_return, 200

    @marshal_with(resource_fields)
    def post(self):
        """ Posts a single Theme. """
        query = theme_queries().insert_query()
        name = request.form['name']
        id_read = request.form['id_reader']
        theme = get_service().post_content(query, [name, id_read])
        if theme is None:
            return abort(400, "The theme could not be created.")
        return ThemeDao(theme), 200
