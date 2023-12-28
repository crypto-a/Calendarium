from flask_restful import Resource
from flask import request
from database.db_setup import init_db



class APIBase(Resource):
    @flask_app.before_first_request
    def get(self):
        """Programmer: Ali Rahbar
        Date: December 20, 2023
        Returns a text to confirm the api system is active.
        """
        init_db()

        message = "Welcome to the api interface of Calendarium."

        return message