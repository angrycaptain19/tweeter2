from flask import Blueprint, jsonify, make_response, request

from ..db.db_posts import (db_create_post, db_delete_post, db_get_all_posts,
                           db_get_one_post, db_update_post)

posts = Blueprint('/api/posts', __name__)

@posts.route("/api/posts", methods=["GET"])
def get_all_posts(current_user):        
    return make_response(jsonify(db_get_all_posts()), 200)
        
@posts.route("/api/posts/<post_id>", methods=["GET"])
def get_one_post(current_user, post_id):
    return make_response(jsonify(db_get_one_post(post_id)), 200)

@posts.route("/api/posts", methods=["POST"])
def create_post(current_user):    
    if request.is_json:
        if(request.method == "POST"):
            _content = request.get_json()["content"]

            print(current_user)

            db_create_post(current_user["public_id"], _content)

            return make_response(jsonify({"message": "Success"}), 200)
    else:
        return make_response(jsonify({"message": "Request body must be JSON"}), 400)

@posts.route("/api/posts", methods=["PATCH"])
def update_post(current_user):
    if request.is_json:
        _data = request.get_json()
        _post_id = _data["post_id"]
        _new_content = _data["new_content"]

        db_update_post(_post_id, _new_content)

        return make_response(jsonify({"message": "Success"}), 200)
    else:
        return make_response(jsonify({"message": "Request body must be JSON"}), 400)

@posts.route("/api/posts/<post_id>", methods=["DELETE"])
def delete_post(current_user, post_id):
    db_delete_post(post_id)

    return make_response(jsonify({"message": "Success"}), 200)
