"""
File: Server.py
Programmer: Ali Rahbar
Date: December 16, 2023
Description: This file is incharge of starting up the calendarium backend server.
"""
import time

from flask import Flask
from flask_cors import CORS
from app import app
from database.db import db
import threading
from Calendarium.SyncMod import start_sync
import os
from flask import Flask, request, g
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import threading
from database.db_transactions import db_transaction
from database.models import User

# Set the status of the debugger
DEBUG = True
PORT = int(os.getenv('PORT', 44000))

# Start the app
flask_app = Flask(__name__, static_url_path='', template_folder='templates')
flask_app.config.from_pyfile('config.py')
flask_app.secret_key = "flask rocks!"  # ToDo: Move to an environment variable

db.init_app(flask_app)

CORS(flask_app)
print('this is server', id(db))


# def background_task():
#     db_trans = db_transaction()
#
#     data_query = User.query.filter_by(username='rahbaral')
#     user = db_trans.select_from_table_first_query(data_query)
#
#     print(user.first_name)


def run_flask():
    """
    Run the flask webserver and prepares the database
    """
    global flask_app

    # Start the flaks app
    flask_app.register_blueprint(app.api_bp, url_prefix='/api')
    flask_app.run(host='0.0.0.0', port=PORT, debug=True)


if __name__ == '__main__':

    # synchronization_thread = threading.Thread(target=background_task)
    # synchronization_thread.start()

    run_flask()
