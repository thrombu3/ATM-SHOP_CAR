from db.db_handle import select_user, save_user_dict as save_user
from datetime import datetime
from lib.common import get_logger


def compute_shop_car(shop_car_dic, product_name, num, price):
    if shop_car_dic.get(product_name, False):
        shop_car_dic[product_name][0] += num
    else:
        shop_car_dic[product_name] = [num, price]
    return shop_car_dic


def append_user_shop_car(username, shop_car_dic):
    res = select_user(username)
    user_shop_car_dic = res["shop_car"]
    car_dic = {}
    for product_name in shop_car_dic.keys():
        car_dic = compute_shop_car(user_shop_car_dic, product_name, shop_car_dic[product_name][0], shop_car_dic[product_name][1])
    res["shop_car"] = car_dic
    save_user(res)
    return True


def append_shop_car_dic(username, shop_car_dic, input_str, input_num, product_name):
    shop_car_dic = compute_shop_car(shop_car_dic, input_str, input_num, product_name)
    logger = get_logger('添加购物车')
    logger.debug(f'用户:{username}把商品{input_str}添加购物车')
    print('添加购物车成功')


def clear_shop_car(input_clear, res):
    if input_clear == 'yes':
        username = res.get("username")
        res['shop_car'] = {}
        logger = get_logger('清空购物车')
        logger.debug(f'用户:{username}清空购物车')
        return_str = '清空成功'
    else:
        return_str = '金额不足'
    return return_str


def show_shop_car(username):
    res = select_user(username)
    car_amount = 0
    print('--------------------------------------------')
    for k, v in res.get('shop_car').items():
        print(f'''          商品名称: %s
              单价: %s
              数量: %s
    --------------------------------------------''' % (k, v[0], v[1]))
        car_amount += (v[0] * v[1])
    print('购物车总金额: %s' % (car_amount))
    return car_amount, res


def clear_user_shop_car(user_dict, car_amount):
    username = user_dict.get("username")
    if car_amount > user_dict.get('balance'):
        input_clear = input('是否清空购物车: yes or no ')
        return_str = clear_shop_car(input_clear, user_dict)
    else:
        user_dict['balance'] -= car_amount
        user_dict['shop_car'] = {}
        user_dict['streams'][datetime.now().strftime('%Y-%m-%d %X')] = [username, '计算购物车', car_amount]
        logger = get_logger('结算购物车')
        logger.debug(f'用户:{username}结算购物车成功')
        return_str = '结算成功'
    save_user(user_dict)
    return return_str
