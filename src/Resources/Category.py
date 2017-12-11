# coding: utf-8

from flask import g, request, Response, jsonify
from flask_restful import Resource,  marshal_with, abort

from models import ThemeDao

from parsers import category_fields

from utils import session


class Category(Resource):
    """ Flask_restful Resource for Category entity, for routes with a parameter. """

    @marshal_with(category_fields)
    def get(self, cat_id):
        """ Returns a single Category. """

        category = session().query(CategoryDao).filter(CategoryDao.id == cat_id)

        if category is None:
            abort(404, message="Category {} does not exist.".format(cat_id))

        return CategoryDao(category), 200

    def delete(self, cat_id):
        """ Deletes a single Category. """

        if session().query(CategoryDao).filter(CategoryDao.id == cat_id).delete():
            abort(404, message="Category {} does not exist.".format(cat_id))

        session().commit()
        return '', 200

    def put(self, cat_id):
        """ Edits a single Category. """

        data = request.json
        theme = session().query(CategoryDao).filter(CategoryDao.id == cat_id)

        if category is None():
            abort(404, message="Category not found.")

        category = format_update_category(category, data)
        session().commit()

        return '', 200


class CategoryList(Resource):
    """ Flask_restful Resource for Category entity, for routes with no parameter."""

    @marshal_with(category_fields)
    def get(self):
        """ Returns every single Category. """
        categories = session().query(CategoryDao).all()

        if categories is None:
            abort(404, "No category in database.")

        array_to_return = []
        
        for e in categories:
            array_to_return.append(CategoryDao(e))

        return array_to_return, 200

    @marshal_with(category_fields)
    def post(self):
        """ Posts a single Category. """

        data = request.json
        name = data.get('name')
        id_theme = data.get('id_theme')

        category = CategoryDao(name, id_theme)

        session().add(category)

        if category is None:
            return abort(400, "The category could not be created.")

        session.commit()
        return category, 200


def format_update_category(source_object, parameters):
    
    body = {}

    category.name = parameters.get('name')\
        if parameters.get('name') else source_object.name
    category.id_theme = parameters.get('id_theme')\
        if parameters.get('id_theme') else source_object.id_theme

    return body
