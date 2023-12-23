from flask_restful import Resource
from Authentication.Authentication import Authentication
from flask import request

authentication = Authentication()


class APIUserSignUp(Resource):
    def post(self):
        first_name = request.args.get('first_name')
        last_name = request.args.get('last_name')
        username = request.args.get('username')
        email = request.args.get('email')
        password = request.args.get('password')

        #Create a new User
        authentication.user_signup(first_name, last_name, username, email, password)

        return 201
