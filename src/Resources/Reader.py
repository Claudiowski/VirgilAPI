# coding: utf-8

from flask import g, request, Response, jsonify
from flask_restful import Resource, marshal_with, abort

from parsers import reader_fields

from models import ReaderDao

from utils import session


class Reader(Resource):
    """ Flask_restful Resource for Reader entity, for routes with a parameter. """

    @marshal_with(reader_fields)
    def get(self, read_id):
        """ Returns a single Reader. """

        reader = session().query(ReaderDao).filter(ReaderDao.id == read_id).first()

        if reader is None:
            abort(404, message="Reader {} does not exist.".format(read_id))

        return ReaderDao(reader), 200

    def delete(self, read_id):
        """ Deletes a single Reader. """

        if not session().filter(Reader._id == read_id).delete():
            abort(404, message="Reader {} does not exist.".format(read_id))

        session().commit()
        return '', 200

    def put(self, read_id):
        """ Edits a single Reader. """

        data = request.json
        reader = session().query(ReaderDao).filter(ReaderDao.id == read_id)

        if reader is None():
            abort(404, message="Reader not found.")

        reader = format_update_reader(reader, data)
        session().commit()

        return '', 200


class ReaderList(Resource):
    """ Flask_restful Resource for Reader entity, for routes with no parameter."""

    @marshal_with(reader_fields)
    def get(self):
        """ Returns every single Reader. """

        reader = session().query(ReaderDao).all()

        if readers is None:
            abort(404, "No reader in database.")

        array_to_return = []
        for e in readers:
            array_to_return.append(ReaderDao(e))

        return array_to_return, 200

    @marshal_with(reader_fields)
    def post(self):
        """ Posts a single Reader. """

        data = request.json()

        pseudo = data.get('pseudo')
        pwd = data.get('password')
        secret = data.get('secret')

        reader = ReaderDao('pseudo', 'password', 'secret')
        session().add(reader)

        if reader is None:
            return abort(400, "The reader could not be created.")

        session().commit()
        return reader, 200


def format_update_reader(source_object, parameters):
    
    body = {}

    reader.pseudo = parameters.get('pseudo')\
        if parameters.get('pseudo') else source_object.pseudo
    reader.password = parameters.get('password')\
        if parameters.get('password') else source_object.password
    reader.secret = parameters.get('secret')\
        if parameters.get('secret') else source_object.secret

    return body
