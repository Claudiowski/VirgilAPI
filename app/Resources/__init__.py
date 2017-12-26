# coding: utf-8

from .Token     import *
from .Reader    import *
from .Theme     import *
from .Category  import *
from .Stream    import *
from .Favorite  import *


def register_endpoints(api):
    
    api.add_resource(Token, '/token')
    api.add_resource(Authentication, '/authentication')

    api.add_resource(ReaderList, '/readers')
    api.add_resource(Reader, '/readers/<int:id_reader>')

    api.add_resource(ThemeList, '/themes', endpoint='themes')
    api.add_resource(ThemeList, '/reader/<int:id_reader>/themes', endpoint='themes_by_reader')
    api.add_resource(Theme, '/themes/<int:id_theme>')

    api.add_resource(CategoryList, '/categories', endpoint='categories')
    api.add_resource(CategoryList, '/theme/<int:id_theme>/categories', endpoint='categories_by_theme')
    api.add_resource(Category, '/categories/<int:id_cat>')

    api.add_resource(StreamList, '/streams', endpoint='streams')
    api.add_resource(StreamList, '/reader/<int:id_reader>/streams', endpoint='streams_by_reader')
    api.add_resource(StreamList, '/theme/<int:id_theme>/streams', endpoint='streams_by_theme')
    api.add_resource(Stream, '/streams/<int:id_stream>')

    api.add_resource(FavoriteList, '/favorites')
    api.add_resource(Favorite, '/favorites/<int:id_fav>')