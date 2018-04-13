from flask_restful import fields

reader_fields = {
    'id':       fields.String(default=None),
    'pseudo':   fields.String(default=None),
    'password': fields.String(default=None),
    'secret':   fields.String(default=None)
}

category_fields = {
    'id':        fields.String(default=None),
    'name':      fields.String(default=None),
    'id_theme':  fields.String(default=None),
}

theme_fields = {
    'id':        fields.String(default=None),
    'name':      fields.String(default=None),
    'id_reader': fields.String(default=None),
    'categories': fields.Nested(category_fields)
}

stream_fields = {
    'id':            fields.String(default=None),
    'url':           fields.String(default=None),
    'name':          fields.String(default=None),
    'id_category':   fields.String(default=None)
}

favorite_fields = {
    'url':         fields.String(default=None),
    'annotation':  fields.String(default=None),
    'id':          fields.String(default=None),
    'id_stream':   fields.String(default=None),
    'title':       fields.String(default=None),
    'description': fields.String(default=None),
    'publication_date':   fields.String(default=None)
}

article_fields = {
    'url':         fields.String(default=None),
    'id':          fields.String(default=None),
    'id_stream':   fields.String(default=None),
    'title':       fields.String(default=None),
    'description': fields.String(default=None),
    'publication_date':   fields.String(default=None),
    'stream':      fields.Nested(stream_fields)
}
