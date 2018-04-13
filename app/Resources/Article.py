# coding: utf-8

import datetime

from flask import g, request, Response, current_app
from flask_restful import Resource, marshal_with, abort, reqparse

from ..models import ArticleDao, StreamDao, CategoryDao, ThemeDao, ReaderDao

from .parsers import article_fields

from datetime import datetime


class Article(Resource):
    """ Flask_restful Resource for Article entity, for routes with a parameter. """

    @marshal_with(article_fields)
    def get(self, id_article):
        """ Returns a single Article. """

        session = current_app.session

        article = session.query(ArticleDao).filter(ArticleDao.id == id_article).first()

        if article is None:
            return None, 204

        return article, 200

    def delete(self, id_article):
        """ Deletes a single Article. """

        session = current_app.session

        if not session.query(ArticleDao).filter(ArticleDao.id == id_article).delete():
            None, 204

        session.commit()
        return '', 200

    def put(self, id_article):
        """ Edits a single Article. """

        session = current_app.session

        data = request.json
        article = session.query(ArticleDao).filter(ArticleDao.id == id_article).first()

        if article is None:
            return None, 204

        article = format_update_article(article, data)
        session.commit()

        return '', 200


class ArticleList(Resource):
    """ Flask_restful Resource for Article entity, for routes with no parameter."""

    @marshal_with(article_fields)
    def get(self, id_reader=None):
        """ Returns every single Article. """

        session = current_app.session

        if id_reader:
            articles = session.query(ArticleDao).join(StreamDao).join(CategoryDao)\
                                .join(ThemeDao).join(ReaderDao)\
                                .filter(ReaderDao.id == id_reader)\
                                .all()


        elif request.args.get('_categories'):
            args = reqparse.RequestParser().add_argument('_categories').parse_args()
            args = args['_categories'].split(',')
            print(args)
            articles = session.query(ArticleDao).join(StreamDao).join(CategoryDao)\
                    .filter(CategoryDao.id.in_(args))\
                    .all()

        elif request.args.get('_themes'):
            args = reqparse.RequestParser().add_argument('_themes').parse_args()
            args = args['_themes'].split(',')
            print(args)
            articles = session.query(ArticleDao).join(StreamDao).join(CategoryDao)\
                    .join(ThemeDao).filter(CategoryDao.id.in_(args))\
                    .all()

        else:
            articles = session.query(ArticleDao).all()

        if len(articles) is 0:
            return None, 204

        return articles, 200

    @marshal_with(article_fields)
    def post(self):
        """ Posts a single Article. """

        session = current_app.session

        data = request.json
        url = data.get('url')
        title = data.get('title')
        description = data.get('description')
        publication_date = data.get('publication_date')
        id_stream = data.get('id_stream')

        article = ArticleDao(annotation=annotation, url=url, title=title, description=description,\
                               publication_date=publication_date, id_stream=id_stream)

        if article is None:
            return None, 202

        session.add(article)
        session.commit()
        return article, 200


def format_update_article(source_object, parameters):
    
    source_object.url = parameters.get('url')\
        if parameters.get('url') else source_object.url
    source_object.title = parameters.get('title')\
        if parameters.get('title') else source_object.title
    source_object.description = parameters.get('description')\
        if parameters.get('description') else source_object.description
    source_object.publication_date = datetime(parameters.get('publication_date'))\
        if parameters.get('publication_date') else source_object.publication_date
    source_object.id_stream = parameters.get('id_stream')\
        if parameters.get('id_stream') else source_object.id_stream

    return source_object