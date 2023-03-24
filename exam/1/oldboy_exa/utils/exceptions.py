# author:liu_ll
from rest_framework.views import exception_handler
from .response import MyResponse
from .logger import get_logger

my_logger = get_logger()


# 全局处理异常
def custom_exception_handler(exc, context):
    # 只要有错就会进入这个函数
    # response为None时这个错是没被捕获的,程序直接抛错代码异常
    response = exception_handler(exc, context)
    if not response:
        # 出了异常
        response = MyResponse(code=5000, msg='服务器错误')
        my_logger.error('服务器错误，错误原因：%s，出错的view是：%s，请求地址是：%s' % (
            str(exc),
            str(context['view']),
            context['request'].path
            # context['request'].get_full_path()
        ))
        return response
    # response不为None时这个错被捕获到了,响应码不是2xx
    response = MyResponse(code=6000, msg=response.data)
    return response
