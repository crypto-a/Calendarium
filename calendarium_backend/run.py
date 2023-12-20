"""
File: run.py
Programmer: Ali Rahbar
Date: December 16, 2023
Description: This file is incharge of starting up the calendarium backend server.
"""
from app import app

DEBUG = True  # Set the status of the debugger

if __name__ == '__main__':
    app.run(debug=DEBUG)
