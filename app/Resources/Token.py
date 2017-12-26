from flask import g, request, Response, current_app
from flask_restful import Resource, abort

from strgen import StringGenerator
import jwt

from ..models import ReaderDao

class Token(Resource):
    """ Flask_restful Resource for Token entity. """

    def get(self):
        """ Return a JWT for the current reader. """

        session = current_app.session

        auth = request.headers.get('Credentials')
        pseudo, passwd = auth.split(':')

        reader = session.query(ReaderDao)\
                            .filter(ReaderDao.pseudo == pseudo, ReaderDao.password == passwd)\
                            .first()

        if reader is not None:
            token, secret = generate_token_and_secret(reader)
            reader.secret = secret
            session.commit()
            return token.decode('utf-8'), 201
        else:
            abort(401, message="No reader for those credentials.")


class Authentication(Resource):
    """ Route to validate authentication. """

    def get(self):
        
        session = current_app.session
        token = request.headers.get('Token')

        reader_id = jwt.decode(token, verify=False)['id']
        secret = session.query(ReaderDao.secret).filter(ReaderDao.id == reader_id).first()[0]

        try:
            jwt.decode(token, secret)
        except:
            abort(401, message="Invalid authentication.")

        return '', 200



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