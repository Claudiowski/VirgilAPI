from sqlalchemy.orm import sessionmaker
from flask import g

def session():
    if not hasattr(g, 'session'):
        g.session = Session()
    return g.session