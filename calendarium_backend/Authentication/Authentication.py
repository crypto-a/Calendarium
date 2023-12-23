from database.models import User
from database.db_transactions import db_transaction

# Create the database transaction mod
db_trans = db_transaction()


class Authentication:
    def user_signup(self, first_name, last_name, username, email, password):
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

        # ToDo: Send the user a conformation email

        # Return success status
        return 201
