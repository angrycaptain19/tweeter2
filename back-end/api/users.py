import datetime
import uuid

from flask import Blueprint, jsonify, make_response

from ..db.db_users import db_get_all_users, db_get_one_user

users = Blueprint('/api/users', __name__)

@users.route("/api/users", methods=["GET"])
def get_all_users():
    return make_response(jsonify(db_get_all_users()), 200)
    
@users.route("/api/users/<public_id>", methods=["GET"])
def get_one_user(current_user, public_id):
    user = db_get_one_user(public_id)

    if user:
        return make_response(jsonify(user), 200)
    else:
        return make_response(jsonify({"message": "User not found"}), 404)