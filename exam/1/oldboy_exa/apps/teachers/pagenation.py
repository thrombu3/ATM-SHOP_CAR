from rest_framework.pagination import PageNumberPagination


class TeacherPageNumberPagination(PageNumberPagination):
    # 默认每页显示的条数
    page_size = 5
    # 根据page显示第几页
    page_query_param = 'page'
    # 根据page_size显示每页显示的条数
    page_size_query_param = 'page_size'
    max_page_size = 15
