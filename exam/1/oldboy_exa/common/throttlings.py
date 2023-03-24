from rest_framework.throttling import SimpleRateThrottle

# 1分钟访问一次
class SMSThrottle(SimpleRateThrottle):
    scope = 'sms'
    def get_cache_key(self, request, view):
        phone = request.query_params.get('phone')

        return self.cache_format % {'scope':self.scope,'ident':phone}