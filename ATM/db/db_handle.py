from conf import settings
import os
import json


def select_user(username):
    user_path = os.path.join(settings.DB_PATH, f"{username}.txt")
    if not os.path.exists(user_path):
        return False
    with open(user_path, 'r', encoding="utf8") as f:
        res = json.load(f)
    return res


def save_user_dict(username_dict):
    username = username_dict.get("username")
    user_path = os.path.join(settings.DB_PATH, f"{username}.txt")
    with open(user_path, 'w', encoding="utf8") as f:
        res = json.dump(username_dict, f, ensure_ascii=False)
    return res
