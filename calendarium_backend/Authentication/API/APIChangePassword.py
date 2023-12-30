from flask_restful import Resource
import jwt
from Server import flask_app
from Authentication.Authentication import Authentication
from flask import request
from Authentication.TokenRequired import token_required

authentication = Authentication()


class APIChangePassword(Resource):
    @token_required
    def put(self):
        """
        Allows the user to change their current password
        """
        # get the token from the URL
        token = request.args.get('token')

        # Decodes the token to find the user id
        decoded_token = jwt.decode(token, flask_app.secret_key, algorithms=['HS256'])
        user_id = decoded_token['id']

        # Get the user inputted passwords
        json_data = request.json
        old_password = json_data.get('old_password')
        new_password = json_data.get('new_password')

        # Change the user's password
        result = authentication.change_password(user_id, old_password, new_password)

        # Shows code for result
        return result
