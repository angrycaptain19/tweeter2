from .db_utils import get, put
from datetime import datetime

def create_user(email, username, bio, birthdate, password):
    put("INSERT INTO Users (Email, Username, Bio, Birthdate, Password) VALUES (?, ?, ?, ?, ?)", [email, username, bio, birthdate, password])

def get_all_users():
    users = get("SELECT Id, Email, Username, Bio, Birthdate FROM Users")

    return format_users(users)

def get_user_by_id(user_id):    
    users = get("SELECT Id, Email, Username, Bio, Birthdate FROM Users WHERE Id = (?)", [user_id])

    return format_users(users)

def get_user_by_username(username):
    users = get("SELECT Id, Email, Username, Bio, Birthdate FROM Users WHERE Username = (?)", [username])

    return format_users(users)

def get_user_by_email(email):
    users = get("SELECT Id, Email, Username, Bio, Birthdate FROM Users WHERE Email = (?)", [email])

    return format_users(users)
    
def format_users(users):
    for user in users:
        user["userId"] = user.pop("id")
        user["birthdate"] = datetime.strftime(user["birthdate"], "%Y-%m-%d")

    return users

def get_user_password(user_id):
    result = get("SELECT Password FROM Users WHERE Id = (?)", [user_id])
    return result[0]["password"]

def update_user(user_id, data):
    if data.get("username"):
        put("UPDATE Users SET Username = (?) WHERE Id = (?)", [data["username"], user_id])
    if data.get("email"):
        put("UPDATE Users SET Email = (?) WHERE Id = (?)", [data["email"], user_id])
    if data.get("bio"):
        put("UPDATE Users SET Bio = (?) WHERE Id = (?)", [data["bio"], user_id])
    if data.get("birthdate"):
        put("UPDATE Users SET Birthdate = (?) WHERE Id = (?)", [data["birthdate"], user_id])

def delete_user(user_id):
    put("DELETE FROM Users WHERE Id = (?)", [user_id])
