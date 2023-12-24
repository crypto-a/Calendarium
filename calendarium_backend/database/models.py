"""
File: models.py
Programmer: Ali Rahbar
Date: December 21, 2023
Description: This file holds all the database models used in the project
"""
from database.db import db
from Authentication import PasswordManager
from datetime import datetime


class User(db.Model):
    """
    User Database Model
    """

    __tablename__ = 'user'

    # Table Properties
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    is_active = db.Column(db.Boolean)
    username = db.Column(db.String)
    password_hash = db.Column(db.String)
    salt = db.Column(db.String)

    def __init__(self, firstname=None, lastname=None, email=None, username=None, password=None):
        self.first_name = firstname
        self.last_name = lastname
        self.email = email
        self.is_active = False
        self.username = username
        self.salt = PasswordManager.generate_salt()
        self.password_hash = str(self.generate_password_hash(password))

    def generate_password_hash(self, password: str) -> str:
        """Programmer: Ali Rahbar
        Date: December 21, 2023
        Returns a hash of the password
        """
        return PasswordManager.hash_password(str(password) + self.salt)

    def check_password_hash(self, password: str) -> bool:
        """Programmer: Ali Rahbar
        Date: December 21, 2023
        Returns a boolean of weather the password is correct or not
        """
        return self.generate_password_hash(password + self.salt) == self.password_hash



# class Subscriptions(db.Model):
#     """
#     Model for subscriptions
#     """
#     __tablename__ = 'subscriptions'
#
#     # Table properties
#     subscription_id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users'))
