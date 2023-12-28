import time

from database.db_transactions import db_transaction

from Calendarium.SyncUserData import SyncUserData
from flask import current_app


def start_sync():

    with current_app.app_context():
        db_trans = db_transaction()

        print("Synchronizing is now running")
        sync_user_data = SyncUserData(1)


if __name__ == "__main__":
    start_sync()


