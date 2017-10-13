# coding: utf-8

from flask import jsonify, g, request, session, Response
from flask_restful import Resource, abort

from strgen import StringGenerator
import jwt

from DbAccess.Service import *
from Authentication.Authentication import *


def store_secret(reader_id, secret):
    query = "UPDATE reader SET secret = %s WHERE id = %s"
    return get_service().put_content(query, [secret, reader_id])


def generate_token_and_secret(reader):
    """ Generates a JWT for a user, according to the common standards. """
    secret = StringGenerator("[a-zA-Z1-9]{255}").render()
    header = {
        'alg': 'HS256',
        'typ': 'JWT'
    }
    payload = {
        'id': str(reader[0]),
        'pseud': reader[1],
        'admin': reader[4]
    }
    token = jwt.encode(payload, secret, algorithm='HS256', headers=header)
    return token, secret


class Token(Resource):
    """ Flask_restful Resource for Token entity. """

    def post(self):
        """ Return a JWT for the user. """
        query = "SELECT * FROM reader WHERE password = %s AND pseudo = %s"
        passwd = request.form['password']
        pseudo = request.form['pseudo']
        print(request.form)
        user = get_service().get_content(query, [passwd, pseudo])
        if user is not None:
            token, secret = generate_token_and_secret(user)
            store_secret(user[0], secret)
            return token.decode('utf-8'), 201
        else:
            abort(401, message="No user for those credentials.")



