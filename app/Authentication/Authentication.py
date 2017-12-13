from flask import request, Response

from functools import wraps
import jwt

from utils import session


def get_auth_data():
    token = request.headers.get('Authorization')
    reader_id = jwt.decode(token, verify=False)['id']
    secret = session().query(ReaderDao.secret).filter(ReaderDao.id == reader_id)
    return token, reader_id, secret


def requires_auth(f):
    """ Manages authorization on routes. """

    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            token, reader_id, secret = get_auth_data()
            jwt.decode(token, secret)
            return f(*args, **kwargs)
        except:
            return Response("Error during authentication.")
    return decorated
