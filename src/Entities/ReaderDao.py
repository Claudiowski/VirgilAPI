from flask_restful import fields
from sqlalchemy import Column, Integer, String


resource_fields = {
    'id':       fields.String(default=None),
    'pseudo':   fields.String(default=None),
    'password': fields.String(default=None),
    'secret':   fields.String(default=None)
}

class ReaderDao(Base):
    """ The Reader entity itself. """

    __tablename__ = 'reader'

    _id = Column(Integer, primary_key=True)
    _pseudo = Column(String)
    _password = Column(String)
    _secret = Column(String)

