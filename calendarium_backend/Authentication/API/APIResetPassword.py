from flask_restful import Resource
import jwt
from Server import flask_app
from Authentication.Authentication import Authentication
from flask import request
from Authentication.TokenRequired import token_required

authentication = Authentication()


class APIResetPassword(Resource):
    def post(self):
        """
        Email the user to reset their password
        """
        # Get the username
        json_data = request.json
        username = json_data.get('username')

        # email user
        result = authentication.reset_password(username)

        # return the http code
        return result

