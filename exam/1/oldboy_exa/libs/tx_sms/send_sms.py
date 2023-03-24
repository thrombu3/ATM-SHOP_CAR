from qcloudsms_py import SmsSingleSender
from oldboy_exa.utils.logger import get_logger
from . import settings
import random


logger = get_logger('django')

def get_code():
    code = str(random.randint(100000, 999999))
    return code

def send(phone, code):
    ssender = SmsSingleSender(settings.APPID, settings.APPKEY)
    params = [code]  # 当模板没有参数时，`params = []`
    try:
      result = ssender.send_with_param(86, phone,
          settings.TEMPLATE_ID, params, sign=settings.SMS_SIGN, extend="", ext="")
      if result.get('result') == 0:
          return True
      else:
          logger.warning('手机号:%s, 短信发送失败, 错误原因:%s' % (phone, result.get('errmsg')))
          return False
    except Exception as e:
      logger.warning('手机号:%s, 短信发送失败, 错误原因:%s' % (phone, e))