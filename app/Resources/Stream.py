# coding: utf-8

from flask import g, request, Response, current_app
from flask_restful import Resource, marshal_with, abort

from ..models import StreamDao, CategoryDao, ThemeDao, ReaderDao

from .parsers import stream_fields


class Stream(Resource):
    """ Flask_restful Resource for Stream entity, for routes with a parameter. """

    @marshal_with(stream_fields)
    def get(self, id_stream):
        """ Returns a single Stream. """

        session = current_app.session

        stream = session.query(StreamDao).filter(StreamDao.id == id_stream).first()

        if stream is None:
            return None, 204

        return stream, 200

    def delete(self, id_stream):
        """ Deletes a single Stream. """

        session = current_app.session

        if not session.query(StreamDao).filter(StreamDao.id == id_stream).delete():
            abort(404, message="Stream {} does not exist.".format(id_stream))

        session.commit()
        return '', 200

    def put(self, id_stream):
        """ Edits a single Stream. """

        session = current_app.session
 
        data = request.json
        stream = session.query(StreamDao).filter(StreamDao.id == id_stream).first()

        if stream is None:
            return None, 204

        stream = format_update_stream(stream, data)
        session.commit()

        return '', 200


class StreamList(Resource):
    """ Flask_restful Resource for Stream entity, for routes with no parameter."""

    @marshal_with(stream_fields)
    def get(self, id_reader=None):
        """ Returns every single Stream. """

        session = current_app.session

        if id_reader:
            streams = session.query(StreamDao).join(CategoryDao)\
                                .join(ThemeDao).join(ReaderDao)\
                                .filter(ReaderDao.id == id_reader).all()

        elif request.args.get('_categories'):
            streams = session.query(StreamDao).join(CategoryDao)\
                   .filter(CategoryDao.id.in_(request.args['_categories'])).all()

        elif request.args.get('_themes'):
            streams = session.query(StreamDao).join(CategoryDao)\
                    .join(ThemeDao)\
                    .filter(CategoryDao.id.in_(request.args['_themes'])).all()
                    
        else:
            streams = session.query(StreamDao).all()

        if len(streams) is 0:
            return None, 204

        return streams, 200

    @marshal_with(stream_fields)
    def post(self):
        """ Posts a single Stream. """

        session = current_app.session

        data = request.json
        url = data.get('url')
        name = data.get('name')
        id_cat = data.get('id_category')

        stream = StreamDao(url=url, name=name, id_category=id_cat)

        if stream is None:
            return None, 202

        session.add(stream)
        session.commit()
        return stream, 200


def format_update_stream(source_object, parameters):

    source_object.url = parameters.get('url')\
        if parameters.get('url') else source_object.url
    source_object.name = parameters.get('name')\
        if parameters.get('name') else source_object.name
    source_object.id_category = parameters.get('id_category')\
        if parameters.get('id_category') else source_object.id_category

    return source_object