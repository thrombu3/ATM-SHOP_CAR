# author:liu_ll

# 自定义过滤类,过滤出该老师的学生考卷
from rest_framework.filters import BaseFilterBackend
from students.models import TestPaper
class MyFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        teacher_id = request.query_params.get('teacher_id')
        queryset = TestPaper.objects.filter(test_bank__teachers_id=teacher_id)
        return queryset