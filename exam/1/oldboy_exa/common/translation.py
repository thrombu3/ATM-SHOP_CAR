from rest_framework.views import APIView
from ..utils.api_response import APIResponse
import json
import requests

class TranslationViews(APIView):
    def post(self, request, *args, **kwargs):
        getdate = request.data.get('disease')

        if not (getdate):
            return APIResponse(status=102, msg='不可为空!')
        res =self.translation_date(request)
        if res == getdate:
            return APIResponse(status=101, msg='翻译失败', data_all=res)
        return APIResponse(status=100, msg='翻译成功', data_all=res)

    @classmethod
    def translation_date(self, request):
        url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        getdate = request.data.get('disease')
        print(getdate)
        new_data = {
            'i': getdate,
            'doctype': 'json'
        }

        ret = requests.post(url, data=new_data).content.decode()
        res = json.loads(ret)
        print(res)
        post_date = res['translateResult'][0][0]['tgt']
        return post_date
