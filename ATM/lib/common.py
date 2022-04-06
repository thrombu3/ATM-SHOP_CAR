from conf import settings

import logging
import logging.config
import hashlib


def get_logger(msg):
    LOGGING_DIC = settings.logging_dic()
    logging.config.dictConfig(LOGGING_DIC)
    logger = logging.getLogger(msg)
    return logger


def check_username(func_name):
    def run_func_name(*args, **kwargs):
        from core import src
        if src.global_username_dic.get("username", False):
            res = func_name(*args, **kwargs)
            return res
        else:
            print('未登录,已自动跳转登录')
            return src.login()
    return run_func_name


def check_isdigit(input_num, remark):
    if input_num.isdigit():
        return int(input_num)
    else:
        input_num = input(f'请输入{remark}: ').strip()
        return check_isdigit(input_num, remark)


def encryption_password(username, password):
    md5 = hashlib.md5()
    md5.update(f'{password}'.encode('utf8'))
    md5.update(f'{username + username}'.encode('utf8'))
    return md5.hexdigest()
