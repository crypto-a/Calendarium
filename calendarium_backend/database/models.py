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

    def __init__(self, first_name=None, last_name=None, email=None, username=None, password=None):
        self.first_name = first_name
        self.last_name = last_name
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
        Returns a boolean of whether the password is correct or not
        """
        return self.generate_password_hash(password) == self.password_hash



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

    def __init__(self, user_id=None, subscription_type=None):

        # Check if the subscription value is correct
        if subscription_type not in ['monthly', 'yearly']:
            raise ValueError('Input value type is not supported (Model: Subscription)')

        # Set parameters
        self.user_id = user_id
        self.subscription_type = subscription_type

        # ToDo: Must be modified when the payments are complete
        # Fix date_valid
        if self.subscription_type == 'monthly':
            self.date_valid = datetime.now() + relativedelta(months=1)
        else:
            self.date_valid = datetime.now() + relativedelta(years=1)

    def increment_date_valid(self) -> None:
        """
        Increment date after each payment
        """
        if self.subscription_type == 'monthly':
            self.date_valid += relativedelta(months=1)
        else:
            self.date_valid += relativedelta(years=1)

    def is_subscription_valid(self) -> bool:
        """
        Check if subscription is valid
        """
        return self.date_valid - datetime.now() >= timedelta(0)


class Payment(db.Model):
    """Programmer: Ali Rahbar
    Date: December 24, 2023

    Model for payments
    """
    __tablename__ = 'payments'

    payment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users'))
    subscription_id = db.Column(db.Integer, db.ForeignKey('subscriptions'))
    amount = db.Column(db.Integer)  # Value is in cents
    date_time = db.Column(db.DateTime)
    payment_reference_id = db.Column(db.String)

    def __init__(self, user_id=None, subscription_id=None, amount=None, payment_reference_id=None):
        self.user_id = user_id
        self.subscription_id = subscription_id
        self.amount = amount
        self.date_time = datetime.now()
        self.payment_reference_id = payment_reference_id


class Account(db.Model):
    """Programmer: Ali Rahbar
    Date: December 24, 2023

    Model for accounts
    """
    __tablename__ = 'accounts'

    account_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users'))
    account_type = db.Column(db.String)
    username = db.Column(db.String)
    access_token = db.Column(db.String)

    def __init__(self, user_id=None, account_type=None, username=None, access_token=None):
        # Check if account type is supported
        if account_type not in ['iCloud', 'Google', 'Outlook']:
            raise ValueError('Input value type is not supported (Model: Account)')

        self.user_id = user_id
        self.account_type = account_type

        # ToDo: Add encryption before writing to database
        self.username = username
        self.access_token = access_token
