from flask import request, Response

from functools import wraps
import jwt

from DbAccess.Service import *


def fetch_secret(reader_id):
    query = "SELECT secret FROM reader WHERE id = %s"
    return get_service().get_content(query, [reader_id])[0]


def get_auth_data():
    token = request.headers.get('Authorization')
    reader_id = jwt.decode(token, verify=False)['id']
    secret = fetch_secret(reader_id)
    return token, reader_id, secret


def requires_admin_auth(f):
    """ Authorizes navigation in admin access pages. """
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            token, reader_id, secret = get_auth_data()
            payload = jwt.decode(token, secret)
            if payload['admin']:
                return f(*args, **kwargs)
        except:
            return Response("Error during authentication.")
    return decorated


def requires_basic_auth(f):
    """ Authorizes navigation in admin access pages. """
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            token, reader_id, secret = get_auth_data()
            jwt.decode(token, secret)
            return f(*args, **kwargs)
        except:
            return Response("Error during authentication.")
    return decorated


class NoSecretFoundError(Exception):
    """Exception no secret file is found"""

    def __init__(self):
        self.msg = 'No secret found.'
