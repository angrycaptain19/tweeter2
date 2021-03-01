from datetime import datetime
import secrets

from flask import Blueprint, jsonify, make_response, request

from ..db import db_users
from ..security.sec_utils import generate_token, check_hash, generate_hash, token_required

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
            user = db_users.get_one_user(userId)             
            if user:
                return make_response(jsonify(user), 200)
            else:
                return make_response(jsonify({"message": "User not found"}), 404)
    else:
        result = db_users.get_all_users()
        if not result:
            return make_response(jsonify({"message": "No results found"}), 404)
        else:
            return make_response(jsonify(result), 200)    

@users.route("/api/users", methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        email = data["email"]
        username = data["username"]
        bio = data["bio"]
        birthdate = datetime.strptime(data["birthdate"], "%Y-%m-%d")
        password = generate_hash(data["password"].encode('utf8'))

        try:
            user_exists = db_users.get_user_by_email(email) or db_users.get_user_by_username(username)
            if user_exists:                
                return make_response(jsonify({"message": "Username or password taken"}), 400)
        except:
            pass            
    except:
        return make_response(jsonify({"message": "Incorrect data"}), 400)
    else:
        db_users.create_user(email, username, bio, birthdate, password)
        new_user = db_users.get_user_by_username(username)            
        token = generate_token(new_user[0]["userId"])
        new_user[0].update({"loginToken": token})
        return make_response(jsonify(new_user), 201)

@users.route("/api/users", methods=["PATCH"])
@token_required
def update_user(user_id):
    data = request.get_json()
    allowed_fields = {"email", "username", "bio", "birthdate"}
    new_data = dict(filter(lambda elem: elem[0] in allowed_fields, data.items()))
    print(data)
    print(new_data)

    if new_data:
        db_users.update_user(user_id, data)
    else:
        return make_response(jsonify({"message": "Incorrect data"}), 400)

    return make_response(jsonify({"message": "User updated"}), 200)
