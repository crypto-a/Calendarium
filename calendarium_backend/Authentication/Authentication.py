import models

from calendarium_backend.database.models import User


class Authentication:

    def user_signup(self, first_name, last_name, username, email, password):
        """
        Programmer: Benjamin Gavriely
        Date: December 23, 2023
        Creates a new user with the sign up information
        """
        return User(first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=email,
                        password=password)

    pass