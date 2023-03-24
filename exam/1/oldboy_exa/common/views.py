# author:liu_ll
from rest_framework.views import APIView
from administrator.models import Admins
from students.models import Students
from teachers.models import Teachers
from oldboy_exa.utils.response import MyResponse
from rest_framework_jwt.utils import jwt_payload_handler
from rest_framework_jwt.utils import jwt_encode_handler
from .authentication import MyJSONWebTokenAuthentication
from oldboy_exa.libs.tx_sms.send_sms import get_code, send
from .throttlings import SMSThrottle
from django.core.cache import cache
from django.conf import settings


class LoginViews(APIView):
    def post(self, request, *args, **kwargs):
        login_type = request.query_params.get('type')
        username = request.data.get('username')
        password = request.data.get('password')
        obj = None
        if not (username and password):
            return MyResponse(code=101, msg='账号和密码必须输入')
        try:
            if login_type == 'student':
                obj = Students.objects.get(username=username, password=password)
            elif login_type == 'teacher':
                obj = Teachers.objects.get(username=username, password=password)
            elif login_type == 'admin':
                obj = Admins.objects.get(username=username, password=password)
            else:
                raise
        except Exception:
            return MyResponse(code=102, msg='账号或密码错误')
        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return MyResponse(code=100, msg='登录成功',
                          data={'token': token, 'user_id': obj.id, 'name': obj.name, 'role_id': obj.role_id,
                                'role_name': obj.role_name})


class VerifyLoginViews(APIView):
    authentication_classes = [MyJSONWebTokenAuthentication, ]

    def get(self, request, *args, **kwargs):
        return MyResponse(msg='ok')


class SendCodeView(APIView):
    def post(self, request, *args, **kwargs):
        global mobile
        user_id = request.data.get('user_id')
        role_id = request.data.get('role_id')
        try:
            if role_id == '0':
                mobile = Admins.objects.values('mobile').filter(id=user_id).first()
            elif role_id == '1':
                mobile = Teachers.objects.values('mobile').filter(id=user_id).first()
            elif role_id == '2':
                mobile = Students.objects.values('mobile').filter(id=user_id).first()
        except Exception as e:
            return MyResponse(code=102, msg='用户不存在!')
        code = get_code()
        print(code)
        res = send(mobile['mobile'], code)
        cache.set(settings.SMS_PHONE_CACHE % mobile['mobile'], code, 60)
        # cache.set(settings.SMS_PHONE_CACHE % mobile['mobile'], '111111', 60)
        if res:
            return MyResponse(msg='短信发送成功, 请及时查收验证码, 您的验证有效期为1分钟!', data=mobile['mobile'])
        else:
            return MyResponse(code=102, msg='短信发送失败!')


class ChangePasswordView(APIView):
    def post(self, request, *args, **kwargs):
        role_id = request.data.get('role_id')
        user_id = request.data.get('user_id')
        password = request.data.get('password')
        checkpassword = request.data.get('checkpassword')
        mobile = request.data.get('mobile')
        code = request.data.get('code')

        if password != checkpassword:
            return MyResponse(code=101, msg='两次密码不匹配!')

        user_code = cache.get(settings.SMS_PHONE_CACHE % mobile)
        # user_code = '111111'
        print(type(code))
        if user_code:
            if str(code) == user_code:
                print(123)
                try:
                    if role_id == '0':
                        Admins.objects.filter(id=user_id).update(password=password)
                    elif role_id == '1':
                        Teachers.objects.filter(id=user_id).update(password=password)
                    elif role_id == '2':
                        Students.objects.filter(id=user_id).update(password=password)
                except Exception as e:
                    return MyResponse(code=102, msg='用户不存在!')
                return MyResponse(code=100, msg='用户密码更新成功!')
            return MyResponse(code=104, msg='请重新输入!')
        else:
            return MyResponse(code=103, msg='您输入的验证码有误!')


class CheckOldPassView(APIView):
    def get(self, request, *args, **kwargs):
        global obj
        user_input_oldpass = request.query_params.get('old_pass')
        user_id = request.query_params.get('user_id')
        role_id = request.query_params.get('role_id')

        try:
            if role_id == '0':
                obj = Admins.objects.filter(id=user_id, password=user_input_oldpass).first()
            elif role_id == '1':
                obj = Teachers.objects.filter(id=user_id, password=user_input_oldpass).first()
            elif role_id == '2':
                obj = Students.objects.filter(id=user_id, password=user_input_oldpass).first()
        except Exception as e:
            return MyResponse(code=101, msg='后端错误', data='您输入的密码有误!')
        if obj:
            return MyResponse(code=100)
        else:
            return MyResponse(code=102, msg='用户或密码不匹配', data='您输入的密码有误!')


