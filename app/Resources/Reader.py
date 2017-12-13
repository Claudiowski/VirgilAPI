# coding: utf-8

from flask import g, request, Response, current_app
from flask_restful import Resource, marshal_with, abort

from .parsers import reader_fields

from ..models import ReaderDao


class Reader(Resource):
    """ Flask_restful Resource for Reader entity, for routes with a parameter. """

    @marshal_with(reader_fields)
    def get(self, read_id):
        """ Returns a single Reader. """

        session = current_app.session

        reader = session.query(ReaderDao).filter(ReaderDao.id == read_id).first()

        if reader is None:
            abort(404, message="Reader {} does not exist.".format(read_id))

        return reader, 200

    def delete(self, read_id):
        """ Deletes a single Reader. """

        session = current_app.session

        if not session.query(ReaderDao).filter(ReaderDao.id == read_id).delete():
            abort(404, message="Reader {} does not exist.".format(read_id))

        session.commit()
        return '', 200

    @marshal_with(reader_fields)
    def put(self, read_id):
        """ Edits a single Reader. """
    
        session = current_app.session

        data = request.json
        reader = session.query(ReaderDao).filter(ReaderDao.id == read_id).first()

        if reader is None:
            abort(404, message="Reader not found.")

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

        if readers is None:
            abort(404, "No reader in database.")

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
        session.add(reader)

        if reader is None:
            return abort(400, "The reader could not be created.")

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
