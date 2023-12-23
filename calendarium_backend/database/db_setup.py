from database.db import db


def init_db():
    # Create tables int eh database
    db.create_all()
    db.session.commit()