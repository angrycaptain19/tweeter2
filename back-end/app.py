import json

import mariadb
from flask import Flask
from flask_cors import CORS

from .api_v1.routes.users import users

app = Flask(__name__)

app.config["CORS_HEADERS"] = "Content-Type"
app.register_blueprint(users)
app.debug = True

CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
