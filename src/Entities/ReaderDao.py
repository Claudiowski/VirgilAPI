from flask_restful import fields


resource_fields = {
    'id':       fields.String(default=None),
    'pseudo':   fields.String(default=None),
    'password': fields.String(default=None),
    'secret':   fields.String(default=None)
}


class ReaderDao:
    """ The Reader entity itself. """

    def __init__(self, array):
        """ Builds the entity from a list. """
        self.id = array[0]
        self.pseudo = array[1]
        self.password = array[2]
        self.secret = array[3]
