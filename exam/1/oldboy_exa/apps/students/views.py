from django.shortcuts import render, HttpResponse
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from rest_framework.viewsets import ViewSetMixin, GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from . import models, serializer
from rest_framework.response import Response
from oldboy_exa.utils.response import MyResponse
from oldboy_exa.utils.api_response import APIResponse
import datetime
from students.models import TestPaper, Grade
from teachers.models import TestBank, Subjects
from students.serializer import TestBankSerializer, StudentTestPaperSerializer
from students.filter import MyFilter
from oldboy_exa.common.authentication import MyJSONWebTokenAuthentication
from oldboy_exa.common.permissions import StudentsPermission

# Create your views here.

class SignView(ViewSetMixin, ListCreateAPIView):
    queryset = models.Sign.objects.all()
    serializer_class = serializer.SignModelSerializer

    def list(self, request, *args, **kwargs):
        id = request.query_params.get('id')
        student = models.Sign.objects.filter(students_id=id).first()  # 问题  按student_id
        if student:
            queryset = models.Sign.objects.filter(students_id=id, sign_detail__date_time=datetime.date.today()).all()
            if queryset:
                serializer = self.get_serializer(queryset, many=True)
                is_sign = serializer.data[0].get('is_sign')
                # print(serializer.data[0]['students'].get('age'))
                if is_sign:
                    return APIResponse(status=100, msg='已签到', data_all=serializer.data[0])
            else:
                return APIResponse(status=101, msg='未签到')
        else:
            return APIResponse(status=102, msg='用户不存在')

    def create(self, request, *args, **kwargs):
        ser = self.get_serializer(data=request.data, context={'request': request})
        if ser.is_valid(raise_exception=True):
            is_sign = ser.context['is_sign']
            is_late = ser.context['is_late']
            student_id = ser.context['student_id']
            sign_detail_id = ser.context['sign_detail_id']
            models.Sign.objects.create(is_sign=is_sign, is_late=is_late, students_id=student_id,
                                       sign_detail_id=sign_detail_id)
            return APIResponse(status=100, msg='签到成功!')
        else:
            return APIResponse(status=101, msg='签到失败!')



class SignAllView(ViewSetMixin, ListCreateAPIView):
    queryset = models.Sign.objects.all()
    serializer_class = serializer.SignModelSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return APIResponse(status=100, msg='获取成功!', data_all=response.data)

    def create(self, request, *args, **kwargs):
        later_list = list()
        for i in range(len(request.data['signInfo'])):
            if request.data['signInfo'][i]['is_late']:
                later_list.append({'date': request.data['signInfo'][i]['sign_detail'].get('date_time'),
                                          'name': request.data['signInfo'][i]['students'].get('name')})
        return APIResponse(status=101, data_all=later_list)


class SignDetailView(ViewSetMixin, ListCreateAPIView):
    queryset = models.SignDetail.objects.all()
    serializer_class = serializer.SignDetailModelSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return APIResponse(status=100, msg='获取成功!', data_all=response.data[-5:])

# 考试模块
# 展示学生题库
class TestBankView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = TestBank.objects.filter(is_commit=True).order_by('-date_time')
    serializer_class = TestBankSerializer

    # 加入校验认证和权限
    # authentication_classes = [MyJSONWebTokenAuthentication, ]
    # permission_classes = [StudentsPermission, ]

# 展示学生考试提交的考卷(查询时把学生id传过来?student_id=)
# 查看考试成绩路径再加学生考卷id  /paper_id/
# 修改考试答案路径再加学生考卷id  /paper_id/
class StudentTestPaperView(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = TestPaper.objects.all().order_by('-commit_time')
    serializer_class = StudentTestPaperSerializer

    filter_backends = [MyFilter, ]
    # 路径?student_id=过滤出该学生的考卷
    # is_check='True'添加了就会只查到被批阅的考卷了
    search_fields = ['student_id', 'is_check']

    # 加入校验认证和权限
    # authentication_classes = [MyJSONWebTokenAuthentication, ]
    # permission_classes = [StudentsPermission, ]

    # 提交考卷
    def create(self, request, *args, **kwargs):
        student_id = request.data.get('students')
        test_bank_id = request.data.get('test_bank')
        test_bank = TestBank.objects.filter(pk=test_bank_id).first()
        # 提交试卷前提必须是：老师提交考卷、考卷开始考试和考卷没有结束
        if not (test_bank.is_commit and test_bank.is_start and not test_bank.is_end):
            return MyResponse(code=102, msg='非法操作')
        res = TestPaper.objects.filter(students_id=student_id, test_bank_id=test_bank_id)
        if res:
            return MyResponse(code=101, msg='试卷已提交,只能修改了')
        test_paper_id = super().create(request, *args, **kwargs).data.get('id')
        # 再创建一个对应的成绩表
        Grade.objects.create(test_paper_id=test_paper_id)
        return MyResponse(msg='ok')

    # 修改考卷(patch方法来修改)
    def update(self, request, *args, **kwargs):
        # 考试时间截至了就不可以修改试卷了
        path = request.path
        test_paper_id = path.split('/')[3]
        test_paper = TestPaper.objects.filter(pk=test_paper_id).first()
        if not test_paper:
            return MyResponse(code=101, msg='考卷不存在')
        if test_paper.test_bank.is_end:
            return MyResponse(code=102, msg='考试已经截止,不能修改试卷了')
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data.pop('students')
        serializer.validated_data.pop('test_bank')
        self.perform_update(serializer)
        return MyResponse(msg='ok')


class GetSignNumView(ViewSetMixin, ListAPIView):
    queryset = models.Sign.objects.all()
    serializer_class = serializer.SignAllModelSerializer

    def list(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        sign_num = len(models.Sign.objects.filter(students_id=user_id, is_sign=1))
        no_sign_num = len(models.Sign.objects.filter(students_id=user_id, is_sign=0))
        return APIResponse(status=100, msg='获取成功!', data_all={'sign_num': sign_num, 'no_sign_num': no_sign_num})

class GetSignDataView(ViewSetMixin, ListAPIView):
    queryset = models.Sign.objects.all()
    serializer_class = serializer.SignAllModelSerializer

    def list(self, request, *args, **kwargs):
        month = list()
        day = list()
        data_list = list()
        user_id = request.query_params.get('user_id')
        sign_data = models.Sign.objects.values('sign_time').filter(students_id=user_id, is_sign=1)
        for i in sign_data:
            month.append(str(i['sign_time']).split(' ')[0].split('-')[1])
            day.append(str(i['sign_time']).split(' ')[0].split('-')[2])
        data_list.append({'months': list(set(month)), 'days': day, 'things': '✔️'})
        print(data_list)
        return APIResponse(status=100, msg='获取成功!', data_all=data_list)
