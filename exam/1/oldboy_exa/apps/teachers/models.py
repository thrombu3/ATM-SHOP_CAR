from django.db import models
from oldboy_exa.utils.models import BaseModel
import datetime


# Create your models here.


class Teachers(BaseModel):
    role_id = models.SmallIntegerField(default=1, verbose_name='角色id')
    role_name = models.CharField(max_length=128, default='教师', verbose_name='角色身份')

    class Meta:
        db_table = "teachers_info"
        verbose_name = "教师信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 题库表
class TestBank(models.Model):
    title = models.CharField(max_length=256, verbose_name='样卷名称')
    date_time = models.DateField(auto_now_add=True, verbose_name='出卷日期')
    is_commit = models.BooleanField(default=False, verbose_name='是否提交')
    is_start = models.BooleanField(default=False, verbose_name='是否开始')
    is_end = models.BooleanField(default=False, verbose_name='是否结束')
    exam_end_time = models.DateTimeField(default=datetime.datetime(1998, 10, 13), verbose_name='考试截止时间', blank=True)  # 时间字段取出来也是时间对象

    teachers = models.ForeignKey('Teachers', on_delete=models.DO_NOTHING, verbose_name='出卷老师')

    class Meta:
        db_table = "test_bank"
        verbose_name = "样卷表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def subjects_list(self):
        res = []
        for item in self.subjects.all():
            res.append({'id': item.id, 'question': item.question})
        return res

    def teachers_name(self):
        return self.teachers.name


# 试题表
class Subjects(models.Model):
    subject_types = (
        (0, '单选题'),
        (1, '多选题'),
        (2, '简答题'),
    )

    subject = models.SmallIntegerField(choices=subject_types, default=2, verbose_name='题型')
    question = models.TextField(verbose_name='题目内容')

    teachers = models.ForeignKey('Teachers', on_delete=models.DO_NOTHING, verbose_name='出题老师')
    test_bank = models.ForeignKey('TestBank', verbose_name='关联样卷', related_name='subjects', on_delete=models.CASCADE,
                                  default=None)

    class Meta:
        db_table = "subjects"
        verbose_name = "试题表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question

    def subject_status(self):
        return self.get_subject_display()

    def teachers_name(self):
        return self.teachers.name

    def test_bank_name(self):
        return self.test_bank.title

    def test_bank_is_start(self):
        return self.test_bank.is_start
