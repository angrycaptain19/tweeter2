import sys
from functools import wraps

import flask_login
from flask import redirect, session
from itsdangerous import BadSignature, SignatureExpired
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_bcrypt import generate_password_hash, check_password_hash
from ..secrets import secrets

sys.path.insert(0, "../db")

try:
    from db.db_user import db_get_one_user, db_get_user_by_username
except ImportError:
    print("No Import flask_bcrypt or login_manager from app.py")

class User(flask_login.UserMixin):
    pass

def user_loader(user_id):
    db_user = db_get_one_user(user_id)[0]

    if not db_user:
        return None

    user = User()
    user.id = user_id
    user.is_anonymous = False
    user.is_authenticated = False
    user.is_active = True

    return user


def request_loader(request):
    _data = request.get_json()
    _username = _data["username"]
    _password = _data["password"]

    db_user = db_get_user_by_username(_username)[0]

    if not db_user:
        return None

    user = User()
    user.id = db_user["Id"]
    user.is_anonymous = False
    
    user.is_active = True

    user.is_authenticated = check_password_hash(db_user[0]["password"], _password)

    return user

# Decorators
def token_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    pass
  
  return wrap

# Expiration: 600 seconds = 10 minutes
def generate_auth_token(user_id, expiration = 600):
    s = Serializer(secrets["secret_key"], expires_in = expiration)
    return s.dumps({ "user_id": user_id })

def verify_auth_token(token):
    s = Serializer(secrets["secret_key"])

    try:
        data = s.loads(token)
    except SignatureExpired:
        return None
    except BadSignature:
        return None

    user = db_get_one_user(data["user_id"])

    return user