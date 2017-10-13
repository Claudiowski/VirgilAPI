# coding: utf-8

from flask import g, request, Response, jsonify
from flask_restful import Resource, fields, marshal_with, abort

from DbAccess.Service import *
from Entities.CategoryDao import *


def category_queries():
    """ Gets an instance of CategoryQueries' from the 'g' environment. """
    if not hasattr(g, 'category_queries'):
        g.category_queries = CategoryQueries()
    return g.category_queries


class CategoryQueries:
    """ Manager for Category entity related SQL queries. """
    
    def select_query(self):
        """ Returns a 'SELECT' query for a single Category. """
        return "SELECT * FROM category WHERE id = %s"

    def delete_query(self):
        """ Returns a 'DELETE' query for a single Category. """
        return "DELETE FROM category WHERE id = %s"

    def select_all_query(self):
        """ Returns a 'SELECT' query for a single Category. """
        return "SELECT * FROM category"

    def insert_query(self):
        """ Returns an 'INSERT' query for a single Category. """
        query = "INSERT INTO category(name, id_theme)"
        return query + " VALUES(%s, %s) RETURNING *"

    def update_query(self, key_list):
        """ Returns an 'UPDATE' query for a single Category. """
        temp = ""
        for k in range(len(key_list)):
            temp += key_list[k] + " = %s, "
        return "UPDATE category SET " + temp[:-2] + " WHERE id = %s"


class Category(Resource):
    """ Flask_restful Resource for Category entity, for routes with a parameter. """

    @marshal_with(resource_fields)
    def get(self, cat_id):
        """ Returns a single Category. """
        query = category_queries().select_query()
        category = get_service().get_content(query, [cat_id])
        if category is None:
            abort(404, message="Category {} does not exist.".format(cat_id))
        return CategoryDao(category), 200

    def delete(self, cat_id):
        """ Deletes a single Category. """
        query = category_queries().delete_query()
        value = get_service().del_content(query, [cat_id])
        if value != 1:
            abort(404, message="Category {} does not exist.".format(cat_id))
        return '', 200

    def put(self, cat_id):
        """ Edits a single Category. """
        key_list, value_list = [], []
        for key, value in request.form.items():
            key_list.append(key)
            value_list.append(value)
        value_list.append(cat_id)
        query = category_queries().update_query(key_list)
        value = get_service().put_content(query, value_list)
        if value != 1:
            abort(400, message="The category could not be updated.")
        return '', 200


class CategoryList(Resource):
    """ Flask_restful Resource for Category entity, for routes with no parameter."""

    @marshal_with(resource_fields)
    def get(self):
        """ Returns every single Category. """
        query = category_queries().select_all_query()
        categories = get_service().get_contents(query)
        if categories is None:
            abort(404, "No category in database.")
        array_to_return = []
        for e in categories:
            array_to_return.append(CategoryDao(e))
        return array_to_return, 200

    @marshal_with(resource_fields)
    def post(self):
        """ Posts a single Category. """
        query = category_queries().insert_query()
        name = request.form['name']
        id_theme = request.form['id_theme']
        category = get_service().post_content(query, [name, id_theme])
        if category is None:
            return abort(400, "The category could not be created.")
        return CategoryDao(category), 200
