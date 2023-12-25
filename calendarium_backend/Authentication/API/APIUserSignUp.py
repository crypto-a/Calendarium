from flask_restful import Resource
from Authentication.Authentication import Authentication
from flask import request

authentication = Authentication()


class APIUserSignUp(Resource):
    def post(self):
        """
        API for creating a new user
        """
        json_data = request.json
        # Collect variables
        first_name = json_data.get('first_name')
        last_name = json_data.get('last_name')
        username = json_data.get('username')
        email = json_data.get('email')
        password = json_data.get('password')

        # Create a new User
        result = authentication.user_signup(first_name, last_name, username, email, password)

        # Return conformation code
        return result
