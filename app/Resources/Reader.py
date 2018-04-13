# coding: utf-8

from flask import g, request, Response, current_app
from flask_restful import Resource, marshal_with, abort

from .parsers import reader_fields

from ..models import ReaderDao

from ..authentication import requires_auth


class Reader(Resource):
    """ Flask_restful Resource for Reader entity, for routes with a parameter. """

    @marshal_with(reader_fields)
    def get(self, id_reader):
        """ Returns a single Reader. """

        session = current_app.session

        reader = session.query(ReaderDao).filter(ReaderDao.id == id_reader).first()

        if reader is None:
            return None, 204

        return reader, 200

    def delete(self, id_reader):
        """ Deletes a single Reader. """

        session = current_app.session

        if not session.query(ReaderDao).filter(ReaderDao.id == id_reader).delete():
            return None, 204

        session.commit()
        return '', 200

    @marshal_with(reader_fields)
    def put(self, id_reader):
        """ Edits a single Reader. """
    
        session = current_app.session

        data = request.json
        reader = session.query(ReaderDao).filter(ReaderDao.id == id_reader).first()

        if reader is None:
            return None, 204

        reader = format_update_reader(reader, data)
        session.commit()

        return reader, 200


class ReaderList(Resource):
    """ Flask_restful Resource for Reader entity, for routes with no parameter."""

    @marshal_with(reader_fields)
    def get(self):
        """ Returns every single Reader. """

        session = current_app.session

        readers = session.query(ReaderDao).all()

        if len(readers) is 0:
            return None, 204

        return readers, 200

    @marshal_with(reader_fields)
    def post(self):
        """ Posts a single Reader. """

        session = current_app.session

        data = request.json

        pseudo = data.get('pseudo')
        pwd = data.get('password')
        secret = data.get('secret') or None

        reader = ReaderDao(pseudo=pseudo, password=pwd, secret=secret)

        if reader is None:
            return None, 202

        session.add(reader)
        session.commit()
        return reader, 200


def format_update_reader(source_object, parameters):
    
    source_object.pseudo = parameters.get('pseudo')\
        if parameters.get('pseudo') else source_object.pseudo
    source_object.password = parameters.get('password')\
        if parameters.get('password') else source_object.password
    source_object.secret = parameters.get('secret')\
        if parameters.get('secret') else source_object.secret

    return source_object
