from flask import request
from functools import wraps
import jwt
from Server import flask_app
from app import app


# Token required decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return {'message': 'Token is missing!'}, 403

        try:
            data = jwt.decode(token, flask_app.secret_key, algorithms=['HS256'])
        except:
            return {'message': 'Invalid token!'}, 403

        return f(*args, **kwargs)

    return decorated
