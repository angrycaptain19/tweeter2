from datetime import datetime
import secrets

from flask import Blueprint, jsonify, make_response, request

from ..db.db_users import (db_create_user, db_get_all_users, db_get_one_user,
                           db_get_user_by_username, db_get_user_by_email)
from ..security.sec_utils import check_hash, generate_hash

users = Blueprint('/api/users', __name__)

@users.route("/api/users", methods=["GET"])
def get_users():
    data = request.get_json()
    if data:
        try:
            userId = data["userId"]
        except:
            return make_response(None, 500)
        else:
            user = db_get_one_user(userId)             
            if user:
                return make_response(jsonify(user), 200)
            else:
                return make_response(jsonify({"message": "User not found"}), 404)
    else:
        result = db_get_all_users()
        if not result:
            return make_response(jsonify({"message": "No results found"}), 404)
        else:
            return make_response(jsonify(db_get_all_users()), 200)    

@users.route("/api/users", methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        email = data["email"]
        username = data["username"]
        bio = data["bio"]
        birthdate = datetime.strptime(data["birthdate"], "%Y-%m-%d")
        password = generate_hash(data["password"])

        try:
            user_exists = db_get_user_by_email(email) or db_get_user_by_username(username)
            if user_exists:                
                return make_response(jsonify({"message": "Username or password taken"}), 400)
        except:
            pass            
    except:
        return make_response(jsonify({"message": "Incorrect data"}), 400)
    else:
        db_create_user(email, username, bio, birthdate, password)
        new_user = db_get_user_by_username(username)            
        token = secrets.token_urlsafe(25)
        new_user[0].update({"loginToken": token})
        return make_response(jsonify(new_user), 201)
