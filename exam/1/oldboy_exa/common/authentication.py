# author:liu_ll
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.utils import jwt_decode_handler
import jwt
from rest_framework import exceptions
from administrator.models import Admins
from students.models import Students
from teachers.models import Teachers


class MyJSONWebTokenAuthentication(JSONWebTokenAuthentication):
    def authenticate(self, request):
        # 全局校验时和操作数据库的时候
        # 前端把role_id加在路径后面(存在漏洞风险)
        role_id = request.query_params.get('role_id')
        jwt_value = self.get_jwt_value(request)

        try:
            payload = jwt_decode_handler(jwt_value)
            print(payload)
            if role_id == '0':
                user = Admins.objects.get(id=payload['user_id'], username=payload['username'])
            elif role_id == '1':
                user = Teachers.objects.get(id=payload['user_id'], username=payload['username'])
            elif role_id == '2':
                user = Students.objects.get(id=payload['user_id'], username=payload['username'])
            else:
                raise exceptions.AuthenticationFailed('校验数据错误,请登录')

        except jwt.ExpiredSignature:
            msg = 'token过期,请登录'
            raise exceptions.AuthenticationFailed(msg)
        except jwt.DecodeError:
            msg = '签名错误,请登录'
            raise exceptions.AuthenticationFailed(msg)
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed('认证失败,请登录')
        except Exception:
            raise exceptions.AuthenticationFailed('校验数据错误,请登录')

        return (user, jwt_value)
