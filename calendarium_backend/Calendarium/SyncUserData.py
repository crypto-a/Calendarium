from database import db
from database.models import User
from database.db_transactions import db_transaction

class SyncUserData:
    _user: User
    _accounts: list
    _events: list

    def __init__(self, user_id):
        db_trans = db_transaction()

        data_query = User.query.filter_by(username='rahbaral')
        self._user = db_trans.select_from_table_first_query(data_query)

        print(self._user.first_name)
