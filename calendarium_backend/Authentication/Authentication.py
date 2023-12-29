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
        token = jwt.encode({'id': database_result[0].user_id,
                            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                           flask_app.secret_key)
        # Send a confirmation email to the user
        send_confirmation_email(email, token)

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
        data_query = User.query.filter_by(user_id=user_id)
        database_result = db_trans.select_from_table_first_query(data_query)
        print(database_result)

        # Activate the user's account
        database_result[0].is_active = True
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

    def change_password(self,user_id, old_password, new_password):
        """
        Programmer:Benjamin Gavriely
        Date: December 29, 2023

        Allows the user to change their existing password to a new password
        """

        # Find the user in the database
        data_query = User.query.filter_by(user_id=user_id)
        database_result = db_trans.select_from_table_first_query(data_query)
        print(database_result)

        # Checks if the old password is correct
        if database_result[0].check_password_hash(old_password):
            # Error if the new password is the same as the old password
            if database_result[0].check_password_hash(new_password):
                return {"message": "Your new password cannot be the same as your current password!"}, 403
            else:
                # Change the user's password
                database_result.password_hash = database_result.generate_password_hash(new_password)
                return {"message": "Your password has been changed!"}, 200
        else:
            # If the current password entered was incorrect
            return {"message": "That is not your current password!"}, 401
