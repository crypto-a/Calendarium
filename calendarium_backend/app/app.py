"""
File: app.py
Programmer: Ali Rahbar
Date: December 20, 2023
Description: This file manages the urls of the flask application.
"""
from flask import Blueprint
from flask_restful import Api

from app.API.APIBase import APIBase
from Authentication.API.APIUserSignUp import APIUserSignUp

# create api instance
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Add Resources
api.add_resource(APIBase, "/")

# User Authentication
api.add_resource(APIUserSignUp, "/APISignUp")
