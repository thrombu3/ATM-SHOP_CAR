from db.db_handle import select_user, save_user_dict as save_user
from lib.common import get_logger, encryption_password


def register_select_from_db(username, password):
    if select_user(username):
        return '用户名已存在', False
    input_password = encryption_password(username, password)
    user_dic = {'username': username, 'password': input_password, 'balance': 15000, 'shop_car': {}, 'streams': {},
                'is_admin': False, 'is_close': False, 'loan': 0}
    save_user(user_dic)
    logger = get_logger('注册')
    logger.debug(f'用户:{username}注册成功')
    return '注册成功', True


def login_select_from_db(username, password):
    res = select_user(username)
    if not res:
        return None, False, False
    if res.get("is_close"):
        return None, False, True
    if encryption_password(username, password) == res.get('password'):
        res["loan"] = round(res["loan"] * (1 + 0.5))
        save_user(res)
        logger = get_logger('登录')
        logger.debug(f'用户:{username}登录成功')
        return [res.get("username"), res.get("is_admin")], True, False
    else:
        return None, False, False


def check_streams_from_db(username):
    res = select_user(username)
    print('--------------------------------------------')
    for k, v in res.get('streams').items():
        print(f'''时间: %s 用户: %s %s %s          
--------------------------------------------''' % (k, v[0], v[1], v[2]))
    return True
