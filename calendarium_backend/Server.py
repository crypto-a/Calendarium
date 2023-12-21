"""
File: Server.py
Programmer: Ali Rahbar
Date: December 16, 2023
Description: This file is incharge of starting up the calendarium backend server.
"""
from flask import Flask
from flask_cors import CORS
from app import app
from database.db import db
import os

# Set the status of the debugger
DEBUG = True
PORT = int(os.getenv('PORT', 44400))

# Start the app
flask_app = Flask( __name__, static_url_path='', template_folder='templates')
flask_app.config.from_pyfile('database/config.py')
flask_app.secret_key = "flask rocks!"
db.init_app(flask_app)

CORS(flask_app)
print('this is server', id(db))


def run_flask():
    """
    Run the flask webserver and prepares the database
    """
    global flask_app

    flask_app.register_blueprint(app.api_bp, url_prefix='/api')
    flask_app.run(host='0.0.0.0', port=PORT, debug=False)


if __name__ == '__main__':

    run_flask()
