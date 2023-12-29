from flask_restful import Resource
from Authentication.Authentication import Authentication
from flask import request
authentication = Authentication()


class APIUserSignIn(Resource):
    def post(self):
        """
        API for signing in a user
        """
        print(0)

        json_data = request.json

        # collect variables
        username = json_data.get('username')
        password = json_data.get('password')

        print(0)
        # sign in the user if credentials are correct.
        result = authentication.user_sign_in(username, password)

        # returns the authentication token if user is signed in,
        # error message if incorrect credentials
        return result
