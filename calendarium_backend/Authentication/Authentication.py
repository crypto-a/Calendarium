from database.models import User
from database.db_transactions import db_transaction

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
        new_user = User(first_name, last_name, username, email, password)
        db_trans.insert_to_table(new_user)

        # ToDo: Send the user a confirmation email

        # Return success status
        return 201

    def user_sign_in(self, username, password):
        """
        Programmer: Benjamin Gavriely
        Date: December 23, 2023
        ----
        Signs in the user if the password is correct
        """
        user = User.query.filter_by(username=username).first()

        # If user exists
        if user is None:
            # Return error
            return {"message": "This username does not exist."}, 401

        # Checks if the password is correct
        if user.check_password_hash(password):

            # ToDo: Return the user token and sign user in!!!
            return 200
        else:
            return {"message": "The password is incorrect."}, 401



