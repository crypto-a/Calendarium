"""
File: app.py
Programmer: Ali Rahbar
Date: December 20, 2023
Description: This file manages the urls of the flask application.
"""
from flask import Blueprint
from flask_restful import Api

from app.API.APIBase import APIBase
from database.db_setup import init_db

from Authentication.API.APIUserSignUp import APIUserSignUp
from Authentication.API.APIUserSignIn import APIUserSignIn
from Authentication.API.APIUserAuthenticate import APIUserAuthenticate
from Authentication.API.APIChangePassword import APIChangePassword
from Authentication.API.APIResetPassword import APIResetPassword

# create api instance
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Add Resources
api.add_resource(APIBase, "/")

# User Authentication
api.add_resource(APIUserSignUp, "/APISignUp")
api.add_resource(APIUserSignIn, "/APISignIn")
api.add_resource(APIUserAuthenticate, "/APIUserAuthenticate")
api.add_resource(APIChangePassword, "/APIChangePassword")
api.add_resource(APIResetPassword, '/APIResetPassword')
