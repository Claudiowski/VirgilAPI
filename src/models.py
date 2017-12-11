
from flask_restful import fields
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine

from sqlalchemy.orm import sessionmaker, relationship

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class ReaderDao(Base):
    """ The Reader entity itself. """

    __tablename__ = 'reader'

    id = Column(Integer, primary_key=True)
    pseudo = Column(String)
    password = Column(String)
    secret = Column(String)

    themes = relationship("Theme", backref="reader")


class ThemeDao(Base):
    """ The Theme entity itself. """

    __tablename__ = 'theme'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    id_reader = Column(Integer, ForeignKey('reader.id'))

    categories = relationship("Category", backref="theme")


class CategoryDao(Base):
    """ The Category entity itself. """
    
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = String()
    id_theme = Column(Integer, ForeignKey('theme.id'))

    streams = relationship("Stream", backref="category")


class StreamDao(Base):
    """ The Stream entity itself. """

    __tablename__ = 'stream'

    id = Column(Integer, primary_key=True)
    url = Column(String)
    name = Column(String)
    id_category = Column(Integer, ForeignKey('category.id'))

    favorites = relationship("Favorite", backref="stream")


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

    stream = relationship("Stream", backref="favorite")


engine = create_engine("postgresql://virgil:virgil@localhost/virgildb")
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)