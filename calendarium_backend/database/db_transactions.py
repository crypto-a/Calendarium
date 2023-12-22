from database.models import db
import logging


class db_transaction:

    def insert_to_table(self, input_data):
        try:
            db.session.add(input_data)
            db.session.commit()
            db.session.close()
            return 200
        except Exception as e:
            print(e)
            return 404

    def update_table(self, input_data):
        try:
            input_data = input_data
            db.session.flush()
            db.session.commit()
            db.session.close()
            return 200
        except Exception as e:
            print(e)
            return 404

    def select_from_table_first_query(self, input_data):
        try:
            db.session.close()
            result = db.session.execute(input_data).first()
            db.session.close()
            return result
        except Exception as e:
            print(e)
            return 404

    def select_from_table_all_query(self, input_data):
        try:
            db.session.close()
            result = db.session.execute(input_data, execution_options={"prebuffer_rows": True})
            logging.warning('watch2:' + str(result))
            db.session.close()
            return result
        except Exception as e:
            print(e)
            return 404

    def delete_table(self, input_data):
        try:
            db.session.delete(input_data)
            db.session.commit()
            db.session.close()
            return 200
        except Exception as e:
            print(e)
            return 404

    def delete_row_in_table(self, input_data):
        try:
            db.session.delete(input_data)
            db.session.commit()
            db.session.close()
            return 200
        except Exception as e:
            print(e)
            return 404