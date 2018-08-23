import random
import string
import time

from KanonApp import Zdb


def create_new_user(google_user_id):
    current_date = int(time.time())
    user_id = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
    Zdb.insert("INSERT INTO Users(UserId, GoogleUserId, DateCreated) VALUES (?, ?, ?)",
               (user_id, google_user_id, int(current_date)))
    return user_id


def get_user_token_by_google_id(google_user_id):
    if google_user_id is not None and len(google_user_id) > 0:
        return Zdb.get_simple_value("SELECT UserId FROM Users WHERE GoogleUserID = ?", (google_user_id,))
