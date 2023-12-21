from flask_restful import Resource
from Authentication.Authentication import Authentication
from flask import request

authentication = Authentication()


class APIUserSignUp(Resource):
    def get(self):
        return "Hello World"
