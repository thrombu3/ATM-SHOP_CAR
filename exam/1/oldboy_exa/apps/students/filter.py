# author:liu_ll

# 自定义过滤类,过滤出该学生的试卷
from rest_framework.filters import BaseFilterBackend
from students.models import TestPaper


class MyFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        # print(request.path)
        student_id = request.query_params.get('student_id')
        is_check = request.query_params.get('is_check')
        queryset = TestPaper.objects.filter(students_id=student_id)
        if is_check == 'True':
            # 要查已批阅的考卷
            queryset = TestPaper.objects.filter(students_id=student_id, is_check=True)

        # 说明要查看考试成绩,只有批改了才可以查看(针对get请求)(废弃)
        # if request.path != '/students/student-paper/' and request.method == 'GET':
        #     queryset = TestPaper.objects.filter(students_id=student_id, is_check=True)
        return queryset
