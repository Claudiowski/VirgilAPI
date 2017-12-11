from sqlalchemy.orm import sessionmaker
from flask import g

def make_session():
    if not hasattr(g, 'session'):
        g.session = Session()