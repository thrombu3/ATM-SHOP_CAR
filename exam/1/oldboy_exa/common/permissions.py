# author:liu_ll
from rest_framework.permissions import BasePermission


class TeachersPermission(BasePermission):
    message = '你不是老师,没有权限'

    def has_permission(self, request, view):
        role_id = request.query_params.get('role_id')
        teachers_id = int(request.query_params.get('teachers'))
        teachers_id_p = int(request.data.get('teachers'))  # 如果提交了teachers就要校验
        if role_id != '1':
            return False

        self.message = '权限不足'
        if teachers_id_p and request.user.id != teachers_id_p:
            return False
        if request.user.id == teachers_id and teachers_id:
            return True
        else:
            return False


class StudentsPermission(BasePermission):
    message = '你不是学生,没有权限'

    def has_permission(self, request, view):
        role_id = request.query_params.get('role_id')
        student_id = int(request.query_params.get('student_id'))
        student_id_p = int(request.data.get('students'))  # 如果提交了students就要校验
        if role_id != '2':
            return False

        self.message = '权限不足'
        if student_id_p and request.user.id != student_id_p:
            return False
        if request.user.id != student_id and student_id:
            return False
        return True

