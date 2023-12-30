from database.models import User
from database.db_transactions import db_transaction
from Authentication.SendEmail import send_confirmation_email
import jwt
import datetime
from flask import jsonify
from Server import flask_app

# Create the database transaction mod
db_trans = db_transaction()


class Authentication:
    def user_signup(self, first_name: str, last_name: str, username: str, email: str, password: str):
        """
        Programmer: Benjamin Gavriely
        Date: December 23, 2023
        ----
        Modified By: Ali Rahbar
        Date Modified: December 23, 2023

        Creates a new user with the sign up information
        """

        # Check to see if username already exists
        data_query = User.query.filter_by(username=username)
        database_result = db_trans.select_from_table_first_query(data_query)

        # If user exists
        if database_result is not None:
            # Return error
            return {"message": "The user address already exists!!"}, 409

        # Create a new User and insert it into database
        new_user = User(first_name, last_name, email, username, password)
        db_trans.insert_to_table(new_user)

        # Find the user id
        data_query = User.query.filter_by(username=username)
        database_result = db_trans.select_from_table_first_query(data_query)

        # Create a token to activate the user's account
        token = jwt.encode({'id': database_result[0].user_id,
                            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=100)},
                           flask_app.secret_key)
        # specify the email body
        email_body = ('Please press this link to confirm your Calendarium account!'
                      'http://127.0.0.1:44000/api/APIUserAuthenticate?token=')
        # Send a confirmation email to the user
        send_confirmation_email(email, email_body, token)

        # Return success status
        return 201

    def user_authenticate(self, user_id):
        """
        Programmer: Benjamin Gavriely
        Date: December 28, 2023

        Activates the user's account if the user presses the confirmation link
        sent to their email and their token is still valid
        """
        # Find the user in the database
        data_query = User.query.filter_by(user_id=user_id).first()

        # Checks if the account has already been validated
        if data_query.is_active:
            return {"message": "Your account has already been validated!"}, 200
        else:
            # Activate the user's account
            data_query.is_active = True
            db_trans.update_table(data_query)
            return {"message": "Your account has been validated!"}, 200

    def user_sign_in(self, username, password):
        """
        Programmer: Benjamin Gavriely
        Date: December 23, 2023
        ----
        Modified By: Ali Rahbar
        Date Modified: December 26, 2023

        Signs in the user if the password is correct
        """
        data_query = User.query.filter_by(username=username)
        database_result = db_trans.select_from_table_first_query(data_query)

        # If user exists
        if database_result is None:
            # Return error
            return {"message": "This username does not exist."}, 401

        # Checks if the password is correct
        if database_result[0].check_password_hash(password):

            # Generates an authentication token
            token = jwt.encode({'id': database_result[0].user_id,
                                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                               flask_app.secret_key)

            return jsonify({'token': token})

        else:
            # Error if the password was incorrect
            return {"message": "The password is incorrect."}, 401

    def change_password(self, user_id, old_password, new_password):
        """
        Programmer:Benjamin Gavriely
        Date: December 29, 2023

        Allows the user to change their existing password to a new password
        """

        # Find the user in the database
        data_query = User.query.filter_by(user_id=user_id).first()

        # This is only if the user is resetting their password
        if data_query.check_password_hash('reset_password'):
            # reset the user's password to the new password
            data_query.password_hash = data_query.generate_password_hash(new_password)
            db_trans.update_table(data_query)
            return {"message": "Your password has been changed!"}, 200

        # Checks if the old password is correct
        if data_query.check_password_hash(old_password):
            if old_password == new_password:
                # Error if the new password is the same as the old password
                return {"message": "Your new password cannot be the same as your current password!"}, 403
            else:
                # Change the user's password
                data_query.password_hash = data_query.generate_password_hash(new_password)
                # Commit changes to the database
                db_trans.update_table(data_query)
                return {"message": "Your password has been changed!"}, 200
        else:
            # If the current password entered was incorrect
            return {"message": "That is not your current password!"}, 401

    def reset_password(self, username):
        # Find the user's email
        data_query = User.query.filter_by(username=username).first()

        # Check if the username exists
        if not data_query:
            return {"message": "Your username does not exist!"}, 401
        else:
            # Create a new token to send in the email
            token = jwt.encode({'id': data_query.user_id,
                                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=100)},
                               flask_app.secret_key)
            # Specify the email body
            email_body = ('Please press this link to reset your password!'
                          'http://127.0.0.1:44000/api/APIChangePassword?token=')
            # Email the user to reset their password
            send_confirmation_email(data_query.email, email_body, token)

            # Reset the user's password
            #TODO change this to be more secure
            data_query.password_hash = data_query.generate_password_hash('reset_password')
            db_trans.update_table(data_query)
            return 200



