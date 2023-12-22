"""
File: models.py
Programmer: Ali Rahbar
Date: December 21, 2023
Description: This file holds all the database models used in the project
"""
from db import db
import os
import binascii
import hashlib
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
        self.salt = self.generate_salt()
        self.password = self.hash_password(password)

    def hash_password(self, input_string: str) -> str:
        """Programmer: Ali Rahbart
        Date: December 21, 2023

        Returns the hash value of the string given to it

        >>> model = User()
        >>> model.hash_password("1234")
        '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'

        >>> model.hash_password("Ali")
        '862ef3927a7c8acfd3e79aa547800ef285cd9b13a39f5ec2d47554981cb313c8'
        """
        sha256_hash = hashlib.sha256()

        sha256_hash.update(input_string.encode('utf-8'))
        hashed_string = sha256_hash.hexdigest()

        return hashed_string

    def generate_salt(self) -> str:
        """Programmer: Ali Rahbar
        Date: December 21, 2023

        Returns a randomly generated salt for the security of the passwords.
        """
        salt_length = 16
        salt = os.urandom(salt_length)

        return binascii.hexlify(salt).decode('utf-8')

    def generate_password_hash(self, password:str) -> str:
        """Programmer: Ali Rahbar
        Date: December 21, 2023
        Returns a hash of the password
        """
        return self.hash_password(password + self.salt)

    def check_password_hash(self, password) -> bool:
        """Programmer: Ali Rahbar
        Date: December 21, 2023
        Returns a boolean of weather the password is correct or not
        """
        return self.hash_password(password + self.salt) == self.password_hash

