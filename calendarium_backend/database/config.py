import os


def get_env_variable(name):
    """Programmer: Ali Rahbar
    Date: December 20, 2023
    Returns the environment variables from the operating system
    """
    try:
        return os.environ[name]

    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


# Set up the base directory
basedir = os.path.abspath(os.path.dirname(__file__))

# database for local test (sqlite3)
SQLITE_FILE_PATH = os.path.join(basedir, 'database.db')  # Adjust the database file path as needed
DB_URL = 'sqlite:///{}'.format(SQLITE_FILE_PATH)

# database for production (MySQL)
# ToDo


SQLALCHEMY_DATABASE_URI = DB_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_RECYCLE = 270
SQLALCHEMY_POOL_TIMEOUT = 300
SQLALCHEMY_POOL_SIZE = 10
