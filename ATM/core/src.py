import os

from conf import settings
from interface import user_interface, bank_interface, shop_car_interface, admin_interface
from lib.common import check_isdigit, check_username

global_username_dic = {
    'username': False,
    'is_admin': False
}

product_dic = {
    '挂壁面': 3,
    '印度飞饼': 22,
    '极品木瓜': 666,
    '土耳其土豆': 999,
    '伊拉克拌面': 1000,
    '董卓戏张飞公仔': 2000,
    '仿真玩偶': 10000
}


def register():
    input_username = input('注册的用户名: ').strip()
    input_password = input('请输入密码: ').strip()
    confirm_password = input('请第二次输入密码: ').strip()
    if input_password != confirm_password:
        return '两个密码输入不一致'
    res, is_success = user_interface.register_select_from_db(input_username, input_password)
    return res


def login():
    input_username = input('登录的用户名: ').strip()
    input_password = input('请输入密码: ').strip()
    username_list, is_success, is_close = user_interface.login_select_from_db(input_username, input_password)
    if is_close:
        return '账号已被冻结'
    if not is_success:
        return '账号或密码错误'
    global_username_dic["username"] = username_list[0]
    global_username_dic["is_admin"] = username_list[1]
    print(username_list, global_username_dic)
    return '登录成功'


@check_username
def recharge():
    input_money = check_isdigit(input('请输入充值的金额: ').strip(), '充值的金额')
    bank_interface.compute_balance('+', global_username_dic.get('username'), "充值", input_money)
    return '充值成功'


@check_username
def withdraw():
    input_money = check_isdigit(input('请输入提现的金额: ').strip(), '提现的金额')
    res, is_success = bank_interface.compute_balance('-', global_username_dic.get('username'), '提现', input_money, 5)
    if not is_success:
        return '余额不足'
    return f'提现成功,手续费为{res - input_money}'


@check_username
def transfer():
    input_username = input('请输入转账的人员: ').strip()
    input_money = check_isdigit(input('请输入转账的金额: ').strip(), '转账的金额')
    input_username_path = os.path.join(settings.DB_PATH, f'{input_username}.txt')
    if not os.path.exists(input_username_path):
        return '转账人员不存在'
    res, is_success = bank_interface.compute_balance('-', global_username_dic.get('username'), '转账', input_money)
    if not is_success:
        return '余额不足'
    res, is_success = bank_interface.compute_balance('+', input_username, '转账', input_money)
    return '转账成功'


@check_username
def check_balance():
    balance = bank_interface.select_balance_from_db(global_username_dic.get('username'))
    return f"用户{global_username_dic.get('username')}余额还剩余{balance}"


@check_username
def check_streams():
    user_interface.check_streams_from_db(global_username_dic.get('username'))
    return '查看流水成功'


@check_username
def append_shop_car():
    print('--------------------------------------------')
    for k, v in product_dic.items():
        print(f'''          商品名称: %s
          单价: %s
--------------------------------------------''' % (k, v))
    shop_car_dic = {}
    while True:
        input_str = input('请输入商品名或者退出: ').strip()
        if input_str == '退出':
            shop_car_interface.append_user_shop_car(global_username_dic.get('username'), shop_car_dic)
            break
        elif product_dic.get(input_str, False):
            input_num = check_isdigit(input('请输入购买商品的数量: ').strip(), '购买商品的数量')
            shop_car_interface.append_shop_car_dic(global_username_dic.get('username'), shop_car_dic, input_str,
                                                   input_num, product_dic.get(input_str))
        else:
            print('请输入正确的商品名称或者退出')
    return '已退出'


@check_username
def settlement_shop_car():
    car_amount, user_dict = shop_car_interface.show_shop_car(global_username_dic.get('username'))
    input_settlement = input('是否结算购物车: yes or no ').strip()
    if input_settlement == 'no':
        return '不结算购物车'
    return_str = shop_car_interface.clear_user_shop_car(user_dict, car_amount)
    return return_str


@check_username
def loan():
    input_money = check_isdigit(input('请输入贷款的金额: ').strip(), '贷款的金额')
    res = bank_interface.loan(global_username_dic.get('username'), input_money)
    return res

@check_username
def show_loan():
    res = bank_interface.show_loan(global_username_dic.get('username'))
    return res


@check_username
def admin_function():
    is_admin = admin_interface.check_admin(global_username_dic.get("username"))
    if not is_admin:
        return "没有对应的权限"

    def lock_user():
        input_username = input('请输入冻结的人员: ').strip()
        res = admin_interface.lock_user(input_username)
        return res

    def remove_lock_user():
        input_username = input('请输入解封的人员: ').strip()
        res = admin_interface.remove_lock_user(input_username)
        return res

    def reset_pwd():
        input_username = input('请输入重置的人员: ').strip()
        res = admin_interface.reset_pwd(input_username)
        return res

    def clear_user():
        input_username = input('请输入删除的人员: ').strip()
        res = admin_interface.clear_user(input_username)
        return res

    def give_user_admin():
        input_username = input('请输入需要管理员权限的人员: ').strip()
        res = admin_interface.give_user_admin(input_username)
        return res

    admin_func = {
        '1': lock_user,
        '2': remove_lock_user,
        '3': reset_pwd,
        '4': clear_user,
        '5': give_user_admin
    }

    while True:
        print('''
                1. 冻结用户账号
                2. 解封用户账号
                3. 修改密码
                4. 删除用户
                5. 设置管理员
                6. 退出
            ''')
        choice = input('请输入管理员功能编号: ').strip()
        if admin_func.get(choice, False):
            res = admin_func.get(choice)()
            print(res)
        elif choice == '6':
            break
        else:
            print('请输入对应的功能编号')
    return '退出成功'


func_dic = {
    '1': register,
    '2': login,
    '3': recharge,
    '4': withdraw,
    '5': transfer,
    '6': check_balance,
    '7': check_streams,
    '8': append_shop_car,
    '9': settlement_shop_car,
    '10': loan,
    '11': show_loan,
    '12': admin_function,
}


def run_shop_car():
    while True:
        print('''
        1. 注册
        2. 登录
        3. 充值
        4. 提现
        5. 转账
        6. 查看余额
        7. 查看流水
        8. 购物车
        9. 结算购物车
        10. 贷款
        11. 查看贷款金额
        12. 管理员功能
        13. 退出
        ''')
        choice = input('请输入功能编号: ').strip()
        if func_dic.get(choice, False):
            res = func_dic.get(choice)()
            print(res)
        elif choice == '13':
            break
        else:
            print('请输入对应的功能编号')
