from rest_framework.response import Response

class APIResponse(Response):
    def __init__(self, msg='请求成功', status=100, data_all=None, template_name=None,
                 headers=None, exception=False, content_type=None, **kwargs):

        real_data = {
            'status':status,
            'msg':msg,
            'data_all': data_all
        }
        if kwargs:
            real_data.update(kwargs)
        super().__init__(data=real_data, template_name=template_name, headers=headers,
                         exception=exception, content_type=content_type)