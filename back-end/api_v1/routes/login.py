from flask import Blueprint, jsonify, make_response, request

from ..db import db_users, db_sessions
from ..security.sec_utils import generate_token, check_hash

login = Blueprint('/api/login', __name__)

@login.route("/api/login", methods=["POST"])
def login_user():
    try:
        data = request.get_json()
        email = data["email"]
        password_claim = data["password"].encode('utf8')       

        user = db_users.get_user_by_email(email)
        stored_password = db_users.get_user_password(user[0]["userId"])

        if check_hash(password_claim, stored_password):
            db_sessions.log_user_in(user[0]["userId"])
            token = generate_token(user[0]["userId"])
            user[0].update({"loginToken": token})
            return make_response(jsonify(user), 201)
        else:
            return make_response(jsonify({"message": "Incorrect username or password"}), 400)
    except Exception as e:
        print(e)
        return make_response(jsonify({"message": "Incorrect data"}), 400)
    