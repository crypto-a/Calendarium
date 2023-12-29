from flask_restful import Resource
from Authentication.Authentication import Authentication
from flask import request
import jwt
from Server import flask_app

authentication = Authentication()

class APIUserAuthenticate(Resource):
    def get(self):
        """
            API for authenticating a user account
        """
        # get the user's authentication token
        token = request.args.get('token')

        # Decodes the token to find the user id
        decoded_token = jwt.decode(token, flask_app.secret_key, algorithms=['HS256'])

        # authenticates the user
        result = authentication.user_authenticate(decoded_token['id'])

        # returns a message and a result code
        return result
