from flask import Blueprint, jsonify, make_response, request
from flask_bcrypt import check_password_hash, generate_password_hash

from ..db import db_sessions
from ..db.db_users import db_create_user, db_get_user_by_username
from ..utils.auth_tools import generate_auth_token

auth = Blueprint('/api/auth', __name__)

@auth.route("/register", methods=["POST"])
def register_user():
    _data = request.get_json()
    _username = _data['username']
    _password = _data['password']

    if not _username or not _password:            
        return make_response(jsonify({"message": "Invalid credentials"}), 401)
    
    user = db_get_user_by_username(_username)        

    if user:
        return make_response(jsonify({"message": "Error"}), 401)
    
    _hashed_password = generate_password_hash(_password)   

    db_create_user(_username, _hashed_password)

    return make_response(jsonify({"message": "New user created"}), 201)

@auth.route("/login", methods=["POST"])
def login():
    _data = request.get_json()
    _username = _data['username']
    _password = _data['password']

    if not _username or not _password:            
        return make_response(jsonify({"message": "Invalid credentials"}), 401)
    
    user = db_get_user_by_username(_username)
    
    if not user:
        return make_response(jsonify({"message": "Invalid credentials"}), 401)

    if (check_password_hash(user[0]["password"], _password)):
        token = generate_auth_token(user[0]["id"], 600).decode('ascii')

        # db_sessions.db_create_session((user[0]["id"], token)

        return make_response(jsonify({"token" : token}), 200)
    else:    
        return make_response(jsonify({"message": "Could not verify"}), 500)
    
@auth.route("/logout", methods=["DELETE"])
def logout(session_id):
    db_sessions.db_delete_session(session_id)

    return make_response(jsonify({"message": "Logged out"}), 200)
