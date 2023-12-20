"""
File: routes.py
Programmer: Ali Rahbar
Date: December 16, 2023
Description: This file includes the routes for the backend which will list teh api urls.
"""
from app import app


@app.route('/')
def index():
    return 'Hello, World!'