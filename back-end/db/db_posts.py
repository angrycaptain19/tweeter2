from .db_utils import get, put
from datetime import datetime

def db_get_all_posts():
    return get("SELECT * FROM Posts")

def db_get_one_post(_id):
    return get("SELECT * FROM Posts WHERE Id = (?)", [_id])  

def db_create_post(public_id, content):
    today = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    put("INSERT INTO Posts (User_Id, Content, Created_At) VALUES (?, ?, ?)", [public_id, content, today])

def db_update_post(post_id, new_content):
    today = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    put("UPDATE Posts SET Content = (?), Created_At = (?) WHERE Id = (?)", [new_content, today, post_id])

def db_delete_post(post_id):
    put("DELETE FROM Posts WHERE Id = (?)", [post_id])