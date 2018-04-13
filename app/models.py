
from flask import g, current_app
from flask_restful import fields
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine

from sqlalchemy.orm import sessionmaker, relationship, backref

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class ReaderDao(Base):
    """ The Reader entity itself. """

    __tablename__ = 'reader'

    id = Column(Integer, primary_key=True)
    pseudo = Column(String)
    password = Column(String)
    secret = Column(String)

    themes = relationship("ThemeDao", backref="reader")


class ThemeDao(Base):
    """ The Theme entity itself. """

    __tablename__ = 'theme'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    id_reader = Column(Integer, ForeignKey('reader.id'))

    categories = relationship("CategoryDao", backref=backref("theme", lazy="joined"))


class CategoryDao(Base):
    """ The Category entity itself. """
    
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    id_theme = Column(Integer, ForeignKey('theme.id'))

    streams = relationship("StreamDao", backref="category")


class StreamDao(Base):
    """ The Stream entity itself. """

    __tablename__ = 'stream'

    id = Column(Integer, primary_key=True)
    url = Column(String)
    name = Column(String)
    id_category = Column(Integer, ForeignKey('category.id'))

    favorites = relationship("FavoriteDao", backref="stream")
    streams = relationship("ArticleDao", backref="stream", lazy="joined")


class ArticleDao(Base):
    """ The Article entity itself. """

    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    publication_date = Column(DateTime)
    url = Column(String)
    description = Column(String(1000))
    id_stream = Column(Integer, ForeignKey('stream.id'))


class FavoriteDao(Base):
    """ The Favorite entity itself """

    __tablename__ = 'favorite'

    id = Column(Integer, primary_key=True)
    annotation = Column(String(511))
    url = Column(String)
    title = Column(String)
    description = Column(String(1000))
    publication_date = Column(DateTime)
    id_stream = Column(Integer, ForeignKey('stream.id'))


if __name__ == '__main__':
    
    from config import *

    conf = config['development']

    engine = create_engine(conf.DB_URI + conf.DB_USER + ':'\
             + conf.DB_PASSWORD + '@' + conf.DB_HOST + '/' + conf.DB_NAME)

    Base.metadata.create_all(engine)
