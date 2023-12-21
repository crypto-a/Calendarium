from flask_restful import Resource
from flask import request


class APIBase(Resource):
    def get(self):
        """Programmer: Ali Rahbar
        Date: December 20, 2023
        Returns a text to confirm the api system is active.
        """
        message = "Welcome to the api interface of Calendarium."

        return message
