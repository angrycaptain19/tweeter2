from .db_utils import get, put
from datetime import datetime

def db_create_session(user_id, session_token):
    put("INSERT INTO User_Sessions (User_Id, Session_Token, Expiry) VALUES (?, ?, ?)", [user_id, session_token, ""])

def db_delete_session(session_id):
    put("DELETE FROM User_Sessions WHERE Id = (?)", [session_id])

