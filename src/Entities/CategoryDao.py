from flask_restful import fields


resource_fields = {
    'id':        fields.String(default=None),
    'name':      fields.String(default=None),
    'id_theme':  fields.String(default=None),
    'name_theme': fields.String(default=None)
}


class CategoryDao:
    """ The Category entity itself. """

    def __init__(self, array):
        """ Builds the entity from a list. """
        self.id = array[0]
        self.name = array[1]
        self.id_theme = array[2]
        if len(array) > 3:
            self.name_theme = array[3]
