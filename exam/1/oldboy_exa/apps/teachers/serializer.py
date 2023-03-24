from rest_framework import serializers
from teachers.models import TestBank, Subjects
from students.models import TestPaper


class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ['id', 'question', 'subject_status', 'teachers_name', 'test_bank_name', 'teachers', 'test_bank','test_bank_is_start']
        extra_kwargs = {
            'id': {'read_only': True},
            'subject_status': {'read_only': True},
            'teachers_name': {'read_only': True},
            'test_bank_name': {'read_only': True},
            'test_bank_is_start': {'read_only': True},
            # 'teachers': {'required': True, 'write_only': True},
            # 'test_bank': {'required': True, 'write_only': True},
            'teachers': {'required': True},
            'test_bank': {'required': True},
        }
    # test_bank_id = serializers.IntegerField(write_only=True)


class TestBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestBank
        fields = ['id', 'title', 'date_time', 'is_commit', 'is_start', 'is_end', 'exam_end_time', 'subjects_list',
                  'teachers']
        extra_kwargs = {
            'id': {'read_only': True},
            'date_time': {'read_only': True},
            # 'is_commit': {'read_only': True},
            # 'is_start': {'read_only': True},
            'is_commit': {'required': True},
            'is_start': {'required': True},

            'is_end': {'read_only': True},
            # 'exam_end_time': {'read_only': True},
            # 'exam_end_time': {'required': True},
            'subjects_list': {'read_only': True},
            'teachers': {'write_only': True},
        }
    # subjects = SubjectsSerializer(many=True, read_only=True)


class TeachersTestPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestPaper
        fields = [
            'id',
            'commit_time',
            'answer',
            'is_check',
            'students_name',
            'test_bank_name',
            'teachers_name',
            'subjects_num',
            # 'subjects_list',
            'source',
            'test_bank_is_end',
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'commit_time': {'read_only': True},
            'answer': {'read_only': True},
            'students_name': {'read_only': True},
            'test_bank_name': {'read_only': True},
            'teachers_name': {'read_only': True},
            'subjects_num': {'read_only': True},
            # 'subjects_list': {'read_only': True},
            'is_check': {'required': True},
            'test_bank_is_end': {'read_only': True},
        }


class TeachersEditPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestPaper
        fields = [
            'id',
            'commit_time',
            'answer',
            'students_name',
            'test_bank_name',
            'teachers_name',
            'subjects_list',
            'test_bank_is_end',

            'is_check',
            'source',  # 必填
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'commit_time': {'read_only': True},
            'answer': {'read_only': True},
            'students_name': {'read_only': True},
            'test_bank_name': {'read_only': True},
            'teachers_name': {'read_only': True},
            'subjects_list': {'read_only': True},
            'test_bank_is_end': {'read_only': True},

            'is_check': {'required': True},
        }
