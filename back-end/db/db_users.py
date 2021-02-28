from .db_utils import get, put

def db_create_user(username, password):
    put("INSERT INTO Users (Username, Password) VALUES (?, ?)", [username, password])

def db_get_all_users():
    return get("SELECT Id, Username FROM Users")

def db_get_one_user(user_id):
    return get("SELECT * FROM Users WHERE Id = (?)", [user_id])

def db_get_user_by_username(username):
    return get("SELECT * FROM Users WHERE Username = (?)", [username])