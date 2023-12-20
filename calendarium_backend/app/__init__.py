"""
File: __init__.py
Programmer: Ali Rahbar
Date: December 16, 2023
Description: This file starts the flask app.
"""

from flask import Flask

app = Flask(__name__)

from app import routes
