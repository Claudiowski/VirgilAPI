# coding: utf-8

from flask import g, request, Response, current_app
from flask_restful import Resource,  marshal_with, abort

from ..models import CategoryDao

from .parsers import category_fields


class Category(Resource):
    """ Flask_restful Resource for Category entity, for routes with a parameter. """

    @marshal_with(category_fields)
    def get(self, id_cat):
        """ Returns a single Category. """

        session = current_app.session

        category = session.query(CategoryDao).filter(CategoryDao.id == id_cat).first()

        if category is None:
            return None, 204

        return category, 200

    def delete(self, id_cat):
        """ Deletes a single Category. """

        session = current_app.session

        if not session.query(CategoryDao).filter(CategoryDao.id == id_cat).delete():
            return None, 204

        session.commit()
        return '', 200

    def put(self, id_cat):
        """ Edits a single Category. """

        session = current_app.session

        data = request.json
        category = session.query(CategoryDao).filter(CategoryDao.id == id_cat).first()

        if category is None:
            return None, 204

        category = format_update_category(category, data)
        session.commit()

        return '', 200


class CategoryList(Resource):
    """ Flask_restful Resource for Category entity, for routes with no parameter."""

    @marshal_with(category_fields)
    def get(self, id_theme=None):
        """ Returns every single Category. """

        session = current_app.session

        if id_theme:
            categories = session.query(CategoryDao).filter(CategoryDao.id_theme == id_theme).all()
        else:
            categories = session.query(CategoryDao).all()

        if len(categories) is 0:
            return None, 204

        return categories, 200

    @marshal_with(category_fields)
    def post(self):
        """ Posts a single Category. """

        session = current_app.session

        data = request.json
        name = data.get('name')
        id_theme = data.get('id_theme')

        category = CategoryDao(name=name, id_theme=id_theme)

        if category is None:
            return None, 202

        session.add(category)
        session.commit()
        return category, 200


def format_update_category(source_object, parameters):
    
    source_object.name = parameters.get('name')\
        if parameters.get('name') else source_object.name
    source_object.id_theme = parameters.get('id_theme')\
        if parameters.get('id_theme') else source_object.id_theme

    return source_object
