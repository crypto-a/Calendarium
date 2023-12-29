from flask import request
from functools import wraps
import jwt
from Server import flask_app
from app import app


# Token required decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Authentication logic goes here
        token = request.args.get('Authorization')

        if not token:
            return {'message': 'Token is missing!'}, 403

        try:
            data = jwt.decode(token, flask_app.secret_key)
        except:
            return {'message': 'Invalid token!'}, 403

        return f(*args, **kwargs)

    return decorated
