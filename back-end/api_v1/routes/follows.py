from flask import Blueprint, jsonify, make_response, request
from flask_api import status

from ..db import db_users, db_followings

login = Blueprint('/api/follows', __name__)

@follows.route("/api/follows", methods=["GET"])
def user_follows():
    try:
        data = request.get_json()
        user_id = data["userId"]

        if db_users.get_user_by_id(userId):
            return make_response(jsonify(db_followings.get_follows(user_id)), status.HTTP_404_NOT_FOHTTP_200_OK)
        else:
            return make_response(jsonify({"message": "User not found"}), status.HTTP_404_NOT_FOUND)