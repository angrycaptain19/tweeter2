import json

import flask_login
import mariadb
from flask import Flask, Response, g, jsonify, make_response, request, session
from flask_bcrypt import Bcrypt
from flask_cors import CORS

from .api.posts import posts
from .api.users import users
from .api.auth import auth
from .secrets import secrets

app = Flask(__name__)

app.secret_key = secrets["secret_key"]
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

app.config["CORS_HEADERS"] = "Content-Type"
app.register_blueprint(posts)
app.register_blueprint(users)
app.register_blueprint(auth)


flask_bcrypt = Bcrypt(app)

CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
