# coding: utf-8

from flask import g, request, Response, current_app
from flask_restful import Resource, marshal_with, abort

from ..models import StreamDao

from .parsers import stream_fields


class Stream(Resource):
    """ Flask_restful Resource for Stream entity, for routes with a parameter. """

    @marshal_with(stream_fields)
    def get(self, stream_id):
        """ Returns a single Stream. """

        session = current_app.session

        stream = session.query(StreamDao).filter(StreamDao.id == stream_id)

        if stream is None:
            abort(404, message="Stream {} does not exist.".format(stream_id))

        return StreamDao(stream), 200

    def delete(self, stream_id):
        """ Deletes a single Stream. """

        session = current_app.session

        if session.query(StreamDao).filter(StreamDao.id == stream_id).delete():
            abort(404, message="Stream {} does not exist.".format(stream_id))

        session.commit()
        return '', 200

    def put(self, stream_id):
        """ Edits a single Stream. """

        session = current_app.session
 
        data = request.json
        stream = session.query(StreamDao).filter(StreamDao.id == stream_id)

        if stream is None():
            abort(404, message="Stream not found.")

        stream = format_update_stream(stream, data)
        session.commit()

        return '', 200


class StreamList(Resource):
    """ Flask_restful Resource for Stream entity, for routes with no parameter."""

    @marshal_with(stream_fields)
    def get(self, reader=None):
        """ Returns every single Stream. """

        session = current_app.session

        if reader:
            streams = session.query(StreamDao).join(CategoryDao)\
                                .join(ThemeDao).join(ReaderDao)\
                                .filter(ReaderDao.id == reader)
        else:
            streams = session.query(StreamDao).all()

        if streams is None:
            abort(404, "Streams not found.")

        return streams, 200

    @marshal_with(stream_fields)
    def post(self):
        """ Posts a single Stream. """

        session = current_app.session

        data = request.json
        url = data.get('url')
        name = data.get('name')
        id_cat = data.get('id_category')

        stream = StreamDao(url, name, id_cat)

        session.add(stream)

        if stream is None:
            return abort(400, "The stream could not be created.")

        session.commit()
        return stream, 200


def format_update_stream(source_object, parameters):
    
    body = {}

    stream.url = parameters.get('url')\
        if parameters.get('url') else source_object.url
    stream.name = parameters.get('name')\
        if parameters.get('name') else source_object.name
    stream.id_category = parameters.get('id_category')\
        if parameters.get('id_category') else source_object.id_category

    return body