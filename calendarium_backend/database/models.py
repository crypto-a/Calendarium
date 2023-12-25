"""
File: models.py
Programmer: Ali Rahbar
Date: December 21, 2023
Description: This file holds all the database models used in the project
"""
from database.db import db
from Authentication import PasswordManager
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class User(db.Model):
    """Programmer: Ali Rahbar
    Date: December 24, 2023
    User Database Model
    """

    __tablename__ = 'users'

    # Table Properties
    user_id = db.Column(db.Integer, primary_key=True)
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


class Subscription(db.Model):
    """Programmer: Ali Rahbar
    Date: December 24, 2023
    Model for subscriptions
    """
    __tablename__ = 'subscriptions'

    # Table properties
    subscription_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users'))
    subscription_type = db.Column(db.String)
    date_valid = db.Column(db.DateTime)

    def __init__(self, user_id: int, subscription_type: str):

        # Check if the subscription value is correct
        if subscription_type not in ['monthly', 'yearly']:
            raise ValueError('Input value type is not supported')

        # Set parameters
        self.user_id = user_id
        self.subscription_type = subscription_type

        # ToDo: Must be modified when the payments are complete
        # Fix date_valid
        if self.subscription_type == 'monthly':
            self.date_valid = datetime.now() + relativedelta(months=1)
        else:
            self.date_valid = datetime.now() + relativedelta(years=1)

    def increment_date_valid(self):
        """
        Increment date after each payment
        """
        if self.subscription_type == 'monthly':
            self.date_valid += relativedelta(months=1)
        else:
            self.date_valid += relativedelta(years=1)

    def is_subscription_valid(self):
        """
        Check if subscription is valid
        :return:
        """
        return self.date_valid - datetime.now() >= 0

class Payments(db.Model):
    """Programmer: Ali Rahbar
    Date: December 24, 2023
    Model for payments
    """
    pass