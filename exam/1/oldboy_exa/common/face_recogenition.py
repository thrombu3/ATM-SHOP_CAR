import base64
import cv2
from aip import AipFace
from rest_framework.views import APIView
from ..utils.api_response import APIResponse


class FaceCompareView(APIView):
    def get(self, request, *args, **kwargs):
        val = request.query_params.get('val')
        if val == '1':
            res = self.take_photo(request)
            if type(res) == list:
                return APIResponse(status=101, msg='验证失败!', data_all=res)
        else:
            res = self.face_compare(request)
            if type(res) == list:
                return APIResponse(status=101, msg='验证失败!', data_all=res)
        return APIResponse(status=100, msg='请求成功!', data_all=res)

    @classmethod
    def take_photo(self, request):
        user_id = request.query_params.get('user_id')
        print(type(user_id))
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            k = cv2.waitKey(1)
            if k == 27:
                cv2.destroyAllWindows()
                return ['已取消录入对比!']
            elif k == ord('s') or k == ord('S'):
                cv2.imwrite("前端传来需要认证的图片" % user_id, frame)
                break
            cv2.imshow("capture", frame)
        cap.release()
        cv2.destroyAllWindows()
        return '拍摄成功!正在对比....'

    @classmethod
    def face_compare(self, request):
        """
        人脸识别对比
        :param img1_data:
        :param img2_data:
        :return:
        """
        user_id = request.query_params.get('user_id')
        with open("数据库初始保存的图片", "rb") as f:
            img1_data = f.read()
        with open("前端传来需要认证的图片" % user_id, "rb") as f:
            img2_data = f.read()

        APP_ID = '******'
        API_KEY = '******'
        SECRET_KEY = '******'

        client = AipFace(APP_ID, API_KEY, SECRET_KEY)

        data1 = base64.b64encode(img1_data)
        data2 = base64.b64encode(img2_data)

        image1 = data1.decode()
        image2 = data2.decode()

        imageType = "BASE64"

        client.detect(image1, imageType)
        client.detect(image2, imageType)

        result = client.match([
            {
                'image': image1,
                'image_type': 'BASE64',
            },
            {
                'image': image2,
                'image_type': 'BASE64',
            }
        ])
        similarity = round(result['result'].get('score'), 2)
        if similarity > 90:
            compare_res ='相似度为: %s%%, 身份认证成功!' % similarity
        else:
            compare_res = ['相似度为: %s%%, 身份认证失败!' % similarity]
        print(compare_res)
        return compare_res

