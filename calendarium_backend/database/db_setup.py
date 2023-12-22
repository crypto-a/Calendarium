from db import db


def init_db():
    db.create_all()
    db.session.commit()