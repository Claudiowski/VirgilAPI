from flask_restful import fields


resource_fields = {
    'id':        fields.String(default=None),
    'name':      fields.String(default=None),
    'id_reader': fields.String(default=None)
}


class ThemeDao:
    """ The Theme entity itself. """

    def __init__(self, array):
        """ Builds the entity from a list. """
        self.id = array[0]
        self.name = array[1]
        self.id_reader = array[2]