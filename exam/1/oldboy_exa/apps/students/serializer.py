from rest_framework import serializers
from . import models
import datetime
from rest_framework.exceptions import ValidationError
from teachers.models import TestBank, Subjects
from students.models import TestPaper, Grade



class StudentsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Students
        fields = ['id','name', 'classes', 'age']


class SignDetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SignDetail
        fields = ['id', 'date_time', 'sign_number', 'no_sign_number']


class SignModelSerializer(serializers.ModelSerializer):
    students = StudentsModelSerializer(read_only=True)
    sign_detail = SignDetailModelSerializer(read_only=True, )

    id = serializers.CharField()

    class Meta:
        model = models.Sign
        fields = ['id', 'is_sign', 'is_late', 'sign_time', 'students', 'sign_detail']

    def validate(self, attrs):
        student_id = attrs.get('id')
        today = datetime.date.today()

        student = models.Students.objects.filter(id=student_id).first()
        # 用户存在, 但不一定签过到, 签过到, 但可能是之前的日期
        if student:
            sign_info = models.Sign.objects.filter(students_id=student_id, sign_detail__date_time=today).first()
            sign_number = models.SignDetail.objects.values('sign_number').filter(date_time=today).first()
            if not sign_number:
                sign_number = 0
            else:
                sign_number = sign_number['sign_number']
            if not sign_info:
                models.SignDetail.objects.update_or_create(date_time=today,
                                                           defaults={'sign_number': sign_number + 1,
                                                                     'no_sign_number': 0, })
                sign_detail_id = models.SignDetail.objects.values('id').filter(date_time=today).first()
                self.context['is_sign'] = True
                self.context['is_late'] = False
                self.context['student_id'] = student_id
                self.context['sign_detail_id'] = sign_detail_id['id']
                return attrs
            else:
                raise ValidationError('您已签到!')
        else:
            raise ValidationError('用户不存在')



class SignAllModelSerializer(serializers.ModelSerializer):
    students = StudentsModelSerializer(read_only=True)
    sign_detail = SignDetailModelSerializer(read_only=True, )
    class Meta:
        model = models.Sign
        fields = ['id', 'is_sign', 'is_late', 'sign_time', 'students', 'sign_detail']

# 考试模块
class TestBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestBank
        fields = [
            'id',
            'title',
            'date_time',
            'is_commit',
            'is_start',
            'is_end',
            'exam_end_time',
            'teachers_name',
            'subjects_list',
        ]



class StudentTestPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestPaper
        fields = [
            'id',
            'commit_time',
            'answer',
            'is_check',
            'subjects_list',
            'source',
            'test_bank_name',
            'teachers_name',
            'test_bank_is_end',
            
            'students',
            'test_bank',
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'commit_time': {'read_only': True},
            'is_check': {'read_only': True},
            'subjects_list': {'read_only': True},
            'source': {'read_only': True},
            'test_bank_name': {'read_only': True},
            'teachers_name': {'read_only': True},
            'test_bank_is_end': {'read_only': True},

            'answer': {'required': True},  # 必填
            # 'students': {'write_only': True},
            # 'test_bank': {'write_only': True},
            'students': {'required': True},
            'test_bank': {'required': True},
        }