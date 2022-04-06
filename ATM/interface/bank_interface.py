from db.db_handle import select_user, save_user_dict as save_user
from datetime import datetime
from lib.common import get_logger


def compute_balance(symbol, username, remark, input_balance, handling_fee=0):
    res = select_user(username)
    balance = res["balance"]
    if symbol == '-':
        if res["balance"] < input_balance:
            return None, False
        res["balance"] -= round(input_balance * (1 + handling_fee / 100))
        label = '减少'
    else:
        res["balance"] += input_balance
        label = '增加'
    res['streams'][datetime.now().strftime('%Y-%m-%d %X')] = [username, remark, input_balance]
    save_user(res)
    logger = get_logger(remark)
    logger.info(f'用户:{username}{label}了{balance - res["balance"]}元')
    return balance - res["balance"], True


def select_balance_from_db(username):
    res = select_user(username)
    return res.get("balance")


def loan(username, money):
    res = select_user(username)
    res["loan"] += money
    save_user(res)
    logger = get_logger('贷款')
    logger.info(f'用户:{username}贷款了{money}元')
    return '贷款成功'


def show_loan(username):
    res = select_user(username)
    return res.get("loan")
