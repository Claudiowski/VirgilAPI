from flask import request, Response, abort, current_app

from functools import wraps
import jwt

from .models import ReaderDao


def get_auth_data():
    session = current_app.session
    token = request.headers.get('Authorization')
    reader_id = jwt.decode(token, verify=False)['id']
    secret = session.query(ReaderDao.secret).filter(ReaderDao.id == reader_id).first()['secret']
    return token, secret


def requires_auth(f):
    """ Manages authorization on routes. """

    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            token, secret = get_auth_data()
            jwt.decode(token, secret)
            return f(*args, **kwargs)
        except:
            abort(401)
    return decorated
