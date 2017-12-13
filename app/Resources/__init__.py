# coding: utf-8

from .Token     import *
from .Reader    import *
from .Theme     import *
from .Category  import *
from .Stream    import *
from .Favorite  import *


def register_endpoints(api):
    
    api.add_resource(Token, '/token')

    api.add_resource(ReaderList, '/readers')
    api.add_resource(Reader, '/readers/<int:read_id>')

    api.add_resource(ThemeList, '/themes', endpoint='themes')
    api.add_resource(ThemeList, '/reader/<int:reader>/themes', endpoint='themes_by_reader')
    api.add_resource(Theme, '/themes/<int:theme_id>')

    api.add_resource(CategoryList, '/categories', endpoint='categories')
    api.add_resource(CategoryList, '/theme/<int:theme>/categories', endpoint='categories_by_theme')
    api.add_resource(Category, '/categories/<int:cat_id>')

    api.add_resource(StreamList, '/streams', endpoint='streams')
    api.add_resource(StreamList, '/reader/<int:reader>/streams', endpoint='streams_by_reader')
    api.add_resource(Stream, '/streams/<int:stream_id>')

    api.add_resource(FavoriteList, '/favorites')
    api.add_resource(Favorite, '/favorites/<int:favorite_id>')