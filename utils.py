from functools import wraps
from flask import session


def check_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(session)
        if session.get('logged_in'):
            return func(*args, **kwargs)
        return "you need to login"
    return wrapper
