from flask import g, request, Response, current_app
from flask_restful import Resource, abort

from strgen import StringGenerator
import jwt


class Token(Resource):
    """ Flask_restful Resource for Token entity. """

    def get(self):
        """ Return a JWT for the current reader. """

        session = current_app.session

        auth = request.headers.get('Credentials')
        pseudo, passwd = auth.split(':')

        reader = session.query(ReaderDao)\
                            .filter(ReaderDao.pseudo == pseudo, ReaderDao.password == passwd)\
                            .first_or_none()

        if reader is not None:
            token, secret = generate_token_and_secret(reader)
            reader.secret = secret
            session.commit()
            return token.decode('utf-8'), 201
        else:
            abort(401, message="No reader for those credentials.")


def generate_token_and_secret(reader):
    """ Generates a JWT for a user, according to the common standards. """

    secret = StringGenerator("[a-zA-Z1-9]{255}").render()

    header = {
        'alg': 'HS256',
        'typ': 'JWT'
    }

    payload = {
        'id': reader.id,
        'pseudo': reader.pseudo
    }

    token = jwt.encode(payload, secret, algorithm='HS256', headers=header)
    return token, secret