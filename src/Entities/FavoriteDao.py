from flask_restful import fields


resource_fields = {
    'url':         fields.String(default=None),
    'annotation':  fields.String(default=None),
    'id':          fields.String(default=None),
    'id_stream':   fields.String(default=None),
    'title':       fields.String(default=None),
    'description': fields.String(default=None),
    'date_hour':   fields.String(default=None)
}


class FavoriteDao:
    """ The Favorite entity itself. """

    def __init__(self, array):
        """ Builds the entity from a list. """
        self.url = array[0]
        self.annotation = array[1]
        self.id = array[2]
        self.id_stream = array[3]
        self.title = array[4]
        self.description = array[5]
        self.date_hour = array[6]