from flask_restful import fields


resource_fields = {
    'id':            fields.String(default=None),
    'url':           fields.String(default=None),
    'name':          fields.String(default=None),
    'id_category':   fields.String(default=None),
    'name_category': fields.String(default=None),
    'id_theme':      fields.String(default=None),
    'name_theme':    fields.String(default=None)
}


class StreamDao:
    """ The Stream entity itself. """

    def __init__(self, array):
        """ Builds the entity from a list. """
        self.id = array[0]
        self.url = array[1]
        self.name = array[2]
        self.id_category = array[3]
        if len(array) > 4:
            self.name_category = array[4]
            self.id_theme = array[5]
            self.name_theme = array[6]
