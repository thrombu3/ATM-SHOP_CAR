from db.db_handle import select_user, save_user_dict as save_user
from lib.common import get_logger, encryption_password
from conf import settings
import os


def check_admin(username):
    user_dict = select_user(username)
    if user_dict['is_admin']:
        return True
    return False


def lock_user(username):
    res = select_user(username)
    res["is_close"] = True
    save_user(res)
    logger = get_logger('冻结账号')
    logger.debug(f'用户:{username}已被冻结')
    return "冻结账号成功"


def remove_lock_user(username):
    res = select_user(username)
    if not res.get("is_close"):
        return '该用户未被冻结'
    res["is_close"] = False
    save_user(res)
    logger = get_logger('解封账号')
    logger.debug(f'用户:{username}已被解封')
    return "解封账号成功"


def reset_pwd(username):
    res = select_user(username)
    res["password"] = encryption_password(username, "123456")
    save_user(res)
    logger = get_logger('重置密码')
    logger.debug(f'用户:{username}已被重置密码')
    return "重置密码成功"


def clear_user(username):
    user_path = os.path.join(settings.DB_PATH, f"{username}.txt")
    if not os.path.exists(user_path):
        return '没有此用户无法删除'
    os.remove(user_path)
    logger = get_logger('删除用户')
    logger.debug(f'用户:{username}已被删除')
    return "删除用户成功"


def give_user_admin(username):
    res = select_user(username)
    if res.get("is_admin"):
        return '该用户已是管理员'
    res["is_admin"] = True
    save_user(res)
    logger = get_logger('添加管理员')
    logger.debug(f'用户:{username}已被添加成管理员')
    return "添加管理员成功"
