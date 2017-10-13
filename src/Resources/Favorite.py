# coding: utf-8

import datetime

from flask import g, request, Response, jsonify
from flask_restful import Resource, fields, marshal_with, abort

from DbAccess.Service import *
from Entities.FavoriteDao import *


def favorite_queries():
    """ Gets an instance of  FavoriteQueries' from the 'g' environment. """
    if not hasattr(g, 'favorite_queries'):
        g.favorite_queries = FavoriteQueries()
    return g.favorite_queries


class FavoriteQueries:
    """ Manager for Favorite entity related SQL queries. """
    
    def select_query(self):
        """ Returns a 'SELECT' query for a single Favorite. """
        return "SELECT * FROM favorite WHERE id = %s"

    def delete_query(self):
        """ Returns a 'DELETE' query for a single Favorite. """
        return "DELETE FROM favorite WHERE id = %s"

    def select_all_query(self):
        """ Returns a 'SELECT' query for a single Favorite. """
        return "SELECT * FROM favorite"

    def insert_query(self):
        """ Returns an 'INSERT' query for a single Favorite. """
        query = "INSERT INTO favorite(url, annotation, id_stream, title, description, date_hour)"
        return query + " VALUES(%s, %s, %s, %s, %s, %s) RETURNING *"

    def update_query(self, key_list):
        """ Returns an 'UPDATE' query for a single Favorite. """
        temp = ""
        for k in range(len(key_list)):
            temp += key_list[k] + " = %s, "
        return "UPDATE favorite SET " + temp[:-2] + " WHERE id = %s"


class Favorite(Resource):
    """ Flask_restful Resource for Favorite entity, for routes with a parameter. """

    @marshal_with(resource_fields)
    def get(self, favorite_id):
        """ Returns a single Favorite. """
        query = favorite_queries().select_query()
        favorite = get_service().get_content(query, [favorite_id])
        if favorite is None:
            abort(404, message="Favorite {} does not exist.".format(favorite_id))
        return FavoriteDao(favorite), 200

    def delete(self, favorite_id):
        """ Deletes a single Favorite. """
        query = favorite_queries().delete_query()
        value = get_service().del_content(query, [favorite_id])
        if value != 1:
            abort(404, message="Favorite {} does not exist.".format(favorite_id))
        return '', 200

    def put(self, favorite_id):
        """ Edits a single Favorite. """
        key_list, value_list = [], []
        for key, value in request.form.items():
            key_list.append(key)
            value_list.append(value)
        value_list.append(favorite_id)
        query = favorite_queries().update_query(key_list)
        value = get_service().put_content(query, value_list)
        if value != 1:
            abort(400, message="The favorite could not be updated.")
        return '', 200


class FavoriteList(Resource):
    """ Flask_restful Resource for Favorite entity, for routes with no parameter."""

    @marshal_with(resource_fields)
    def get(self):
        """ Returns every single Favorite. """
        query = favorite_queries().select_all_query()
        favorites = get_service().get_contents(query)
        if favorites is None:
            abort(404, "No favorite in database.")
        array_to_return = []
        for e in favorites:
            array_to_return.append(FavoriteDao(e))
        return array_to_return, 200

    @marshal_with(resource_fields)
    def post(self):
        """ Posts a single Favorite. """
        query = favorite_queries().insert_query()
        url = request.form['url']
        annotation = request.form['annotation']
        id_stream = request.form['id_stream']
        title = request.form['title']
        description = request.form['description']
        date_hour = request.form['date_hour']
        favorite = get_service().post_content(query, [url, annotation, id_stream, title, description, date_hour])
        if favorite is None:
            return abort(400, message="The favorite could not be created.")
        return FavoriteDao(favorite), 200
