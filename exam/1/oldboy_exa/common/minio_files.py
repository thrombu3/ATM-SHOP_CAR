# minio_client.py
import os
from minio import Minio
from minio.error import InvalidResponseError
from rest_framework.views import APIView
from ..utils.api_response import APIResponse



class MinIOFilesView(APIView):
    minioClient = Minio('127.0.0.1:9000',  # 可配置公网
                        access_key='****',
                        secret_key='********',
                        secure=False
                        )

    # # minioClient.make_bucket("mybucket", location="us-east-1")  创建桶
    def post(self, request, *args, **kwargs):
        p_file = request.FILES.getlist("file")
        dir = '文件保存路径/%s'
        if p_file is None:
            return APIResponse(status=101, msg='文件上传失败')
        else:
            for f in p_file:
                with open(dir % str(f.name), 'wb') as fl:
                    for chunk in f.chunks():
                        fl.write(chunk)
                break
        # time.sleep(10)
        res = self.get_file(request)
        if type(res) == list:
            return APIResponse(status=101, mag='上传至本地成功', data_all=res[0])
        return APIResponse(status=100, mag='上传至本地成功', data_all=res)

    @classmethod
    def get_file(self, request):
        dir = '文件保存路径/%s'
        global name
        p_file = request.FILES.getlist("file")
        for f in p_file:
            name = f.name
            if name is None:
                return ['文件丢失请重新上传']
            break
        try:
            with open(dir % name, 'rb') as file_data:
                file_stat = os.stat(dir % name)
                self.minioClient.put_object('mybucket', name, file_data, file_stat.st_size)
            return '文件上传服务器成功'
        except InvalidResponseError as err:
            return '上传至服务器失败!'

    # def post_file(self):  # 文件下载
    #     try:
    #         data = self.minioClient.get_object('mybucket', 'AFei.MOV')
    #         with open('AFei.MOV', 'wb') as f:
    #             for line in data:
    #                 f.write(line)
    #         print(data.read())
    #     except InvalidResponseError as err:
    #         print(err)
