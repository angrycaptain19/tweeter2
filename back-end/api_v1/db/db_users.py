from .db_utils import get, put
from datetime import datetime

def db_create_user(email, username, bio, birthdate, password):
    put("INSERT INTO Users (Email, Username, Bio, Birthdate, Password) VALUES (?, ?, ?, ?, ?)", [email, username, bio, birthdate, password])

def db_get_all_users():
    users = get("SELECT Id, Email, Username, Bio, Birthdate FROM Users")

    return format_users(users)

def db_get_one_user(user_id):    
    users = get("SELECT Id, Email, Username, Bio, Birthdate FROM Users WHERE Id = (?)", [user_id])

    return format_users(users)

def db_get_user_by_username(username):
    users = get("SELECT Id, Email, Username, Bio, Birthdate FROM Users WHERE Username = (?)", [username])

    return format_users(users)

def db_get_user_by_email(email):
    users = get("SELECT Id, Email, Username, Bio, Birthdate FROM Users WHERE Email = (?)", [email])

    return format_users(users)
    
def format_users(users):
    for user in users:
        user["userId"] = user.pop("id")
        user["birthdate"] = datetime.strftime(user["birthdate"], "%Y-%m-%d")

    return users