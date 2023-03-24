from django.shortcuts import render
from oldboy_exa.utils.response import MyResponse
from rest_framework.generics import GenericAPIView, RetrieveAPIView, CreateAPIView, ListAPIView, UpdateAPIView, \
    DestroyAPIView
from rest_framework.viewsets import ViewSetMixin, GenericViewSet, ViewSet
from teachers.models import TestBank, Subjects
from teachers.serializer import TestBankSerializer, SubjectsSerializer, TeachersTestPaperSerializer, \
    TeachersEditPaperSerializer
from django_filters.rest_framework import DjangoFilterBackend
from students.models import TestPaper, Grade
from teachers.filter import MyFilter
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from oldboy_exa.common.authentication import MyJSONWebTokenAuthentication
from oldboy_exa.common.permissions import TeachersPermission
from apscheduler.schedulers.background import BackgroundScheduler
from rest_framework.decorators import action
from rest_framework.response import Response
from teachers.pagenation import TeacherPageNumberPagination


# Create your views here.
# 考试模块

class TestBankView(ViewSetMixin, ListAPIView, CreateAPIView, RetrieveModelMixin, UpdateModelMixin):
    queryset = TestBank.objects.all().order_by('-date_time')
    serializer_class = TestBankSerializer

    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ['teachers', ]

    # 加入校验认证和权限（待测试）
    # authentication_classes = [MyJSONWebTokenAuthentication, ]
    # permission_classes = [TeachersPermission, ]

    def create(self, request, *args, **kwargs):
        if request.data.get('is_commit') != False or request.data.get('is_start') != False:
            return MyResponse(code=101, msg='提交的数据错误')
        response = super().create(request, *args, **kwargs)
        return MyResponse(msg='ok', data=response.data)

    def update(self, request, *args, **kwargs):
        is_commit = request.data.get('is_commit')
        is_start = request.data.get('is_start')
        is_end = request.data.get('is_end')
        if is_end != None:
            return MyResponse(code=101, msg='error1')
        if is_commit != None and is_commit != True:
            return MyResponse(code=102, msg='error2')
        test_bank_id = request.path.split('/')[3]
        test_bank = TestBank.objects.filter(pk=test_bank_id).first()
        if is_start != None:
            if is_start == True:
                import datetime
                exam_end_time = test_bank.exam_end_time  # 考试截止时间
                subjects = Subjects.objects.filter(test_bank=test_bank)
                if not test_bank.is_commit or exam_end_time == datetime.datetime(1998, 10, 13) or not subjects:
                    return MyResponse(code=103, msg='error3')
                else:
                    # 说明开考成功,可以提交一个延时任务
                    # # celery异步框架（有问题）
                    # from oldboy_exa.apps.teachers.teacher_task import update_test_bank
                    # from datetime import datetime, timedelta
                    # eta = exam_end_time - timedelta(hours=8)  # 要用utc时间
                    # res_id = update_test_bank.apply_async(args=(test_bank_id), eta=eta)
                    # # print(res_id)

                    # 使用定时框架APScheduler
                    from oldboy_exa.apps.teachers.teacher_task import update_test_bank
                    from datetime import datetime
                    # print(exam_end_time, type(exam_end_time))  # 2021-05-31 16:33:00 <class 'datetime.datetime'>
                    if exam_end_time <= datetime.today():
                        update_test_bank(test_bank_id)
                    else:
                        scheduler = BackgroundScheduler()
                        scheduler.add_job(update_test_bank, 'date', args=(test_bank_id,), run_date=exam_end_time)
                        scheduler.start()
            else:
                return MyResponse(code=104, msg='error4')
        # 校验一下时间是否合理,必须大于当前时间（不想加）
        exam_end_time = request.data.get('exam_end_time')
        if exam_end_time != None and test_bank.is_start:
            return MyResponse(code=105, msg='error5')
        # print(exam_end_time)
        # print(type(exam_end_time))
        response = super().update(request, *args, **kwargs)
        return MyResponse(msg='ok', data=response.data)


# 修改操作权限校验时根据?后面的teachers（必须传）就可以（考试已开始不能删除和修改，也不能给已经开考的题库创建试题）
# patch局部修改，put全局（全字段修改）(传question,teachers,test_bank)
class SubjectsView(ViewSetMixin, CreateAPIView, ListAPIView, RetrieveModelMixin, UpdateAPIView, DestroyAPIView):
    queryset = Subjects.objects.all().order_by('-id')
    serializer_class = SubjectsSerializer

    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ['teachers', ]

    # 加入校验认证和权限（待测试）
    # authentication_classes = [MyJSONWebTokenAuthentication, ]
    # permission_classes = [TeachersPermission, ]

    def create(self, request, *args, **kwargs):
        teachers_id = request.data.get('teachers')
        test_bank_id = request.data.get('test_bank')
        test_bank = TestBank.objects.filter(pk=test_bank_id).first()
        if test_bank.is_start:
            return MyResponse(code=101, msg='考试已经开考,不能给这个题库添加试题了')
        if test_bank.teachers_id != teachers_id:
            return MyResponse(code=102, msg='你不能给别人的题库添加试题')
        super().create(request, *args, **kwargs)
        return MyResponse(msg='ok')

    def update(self, request, *args, **kwargs):
        # 考试开始就不可以修改考题了
        path = request.path
        subjects_id = path.split('/')[3]
        test_bank_obj = TestBank.objects.filter(subjects__id=subjects_id).first()
        if test_bank_obj.is_start:
            return MyResponse(code=101, msg='考试已经开考,不能修改试题了')
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data.pop('teachers')
        serializer.validated_data.pop('test_bank')
        self.perform_update(serializer)
        return MyResponse(msg='ok')


class TeachersTestPaperView(ViewSetMixin, ListAPIView, RetrieveAPIView):
    queryset = TestPaper.objects.all().order_by('-commit_time')
    serializer_class = TeachersTestPaperSerializer

    filter_backends = [MyFilter, DjangoFilterBackend]
    # 路径?teacher_id=1过滤出该老师出的试卷
    search_fields = ['teacher_id']
    filter_fields = ['test_bank', ]

    pagination_class = TeacherPageNumberPagination

    # 加入校验认证和权限（待测试）
    # authentication_classes = [MyJSONWebTokenAuthentication, ]
    # permission_classes = [TeachersPermission, ]


# patch 改两个表的数据 成绩 和 是否批改(传source,is_check)
class TeachersEditPaperView(GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    queryset = TestPaper.objects.all()
    serializer_class = TeachersEditPaperSerializer

    filter_backends = [MyFilter, ]
    # 路径?teacher_id=1过滤出该老师出的试卷
    search_fields = ['teacher_id']

    # 加入校验认证和权限（待测试）
    # authentication_classes = [MyJSONWebTokenAuthentication, ]
    # permission_classes = [TeachersPermission, ]

    def update(self, request, *args, **kwargs):
        path = request.path
        test_paper_id = path.split('/')[3]
        # print(test_paper_id)
        # 再增加一个只有试卷考试结束才可以修改学生成绩
        test_bank = TestBank.objects.filter(testpaper__id=test_paper_id).first()
        if not test_bank.is_end:
            return MyResponse(code=101, msg='考试没结束不能批改')
        print(request.data)
        try:
            source = int(request.data.get('source'))
        except Exception:
            return MyResponse(code=102, msg='提交数据有误')
        super().update(request, *args, **kwargs)
        Grade.objects.filter(test_paper_id=test_paper_id).update(source=source)
        return MyResponse(msg='ok', data={'source': source, 'test_paper_id': test_paper_id})


class TeacherCommonView(ViewSet):
    # 加入校验认证和权限（待测试）
    # authentication_classes = [MyJSONWebTokenAuthentication, ]
    # permission_classes = [TeachersPermission, ]

    # 获得老师的题库id和title
    @action(methods=['GET'], detail=False)
    def get_teachers_test_bank(self, request, *args, **kwargs):
        teachers_id = request.query_params.get('teachers')
        res = TestBank.objects.filter(teachers_id=teachers_id).values('id', 'title')
        # print(res)
        # test_bank_list = []
        # for item in res:
        #     test_bank_list.append(item[0])
        # test_bank_list = [item[0] for item in res]
        # return Response(test_bank_list)
        return Response(res)


import json


# 测试使用接口
class TestView(ViewSet):
    # 批量创建考卷
    @action(methods=['GET'], detail=False)
    def batch_paper(self, request, *args, **kwargs):
        answer = json.dumps([{"id": 13, "question": "2+2=？", "answer": "4"}])
        paper_list = []
        for id in range(2, 41):
            obj1 = TestPaper(test_bank_id=3, answer=answer, students_id=id)
            paper_list.append(obj1)
        TestPaper.objects.bulk_create(paper_list)
        return MyResponse(msg='ok')

    # 批量创建考卷的成绩
    @action(methods=['GET'], detail=False)
    def batch_grade(self, request, *args, **kwargs):
        grade_list = []
        for id in range(52, 91):
            obj2 = Grade(test_paper_id=id)
            grade_list.append(obj2)
        Grade.objects.bulk_create(grade_list)
        return MyResponse(msg='ok')

    # 只要登录了就可以看（只要配一个认证类）
    # 获取最近的一次考试成绩(首页展示echarts)
    @action(methods=['GET'], detail=False)
    def get_lately_source(self, request, *args, **kwargs):
        test_bank_id = 7
        sources = TestPaper.objects.filter(test_bank_id=test_bank_id, is_check=True).values('grade__source')
        # --50  51-60  61-70  71-80  81-90  91--
        echarts_1 = {'a': {'name': '50分以下', 'count': 0},
                     'b': {'name': '51-60分', 'count': 0},
                     'c': {'name': '61-70分', 'count': 0},
                     'd': {'name': '71-80分', 'count': 0},
                     'e': {'name': '81-90分', 'count': 0},
                     'f': {'name': '91分以上', 'count': 0}}
        echarts_2 = {'a': {'name': '及格率', 'rate': None},
                     'b': {'name': '不及格率', 'rate': None}}
        for item in sources:
            source = item['grade__source']
            if source<=50:
                echarts_1['a']['count'] += 1
            elif 51<=source<=60:
                echarts_1['b']['count'] += 1
            elif 61<=source<=70:
                echarts_1['c']['count'] += 1
            elif 71<=source<=80:
                echarts_1['d']['count'] += 1
            elif 81<=source<=90:
                echarts_1['e']['count'] += 1
            elif source>=91:
                echarts_1['f']['count'] += 1
        # print(echarts_1)
        # data = {''}
        return Response(echarts_1)
