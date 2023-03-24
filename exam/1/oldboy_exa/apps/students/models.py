from django.db import models
from oldboy_exa.utils.models import BaseModel
from teachers import models as te_models


# Create your models here.

class Students(BaseModel):
    class_choices = (
        (0, 'Linux'),
        (1, 'Python'),
        (2, 'Preparatory'),  # 预科班
    )
    role_id = models.SmallIntegerField(default=2, verbose_name='角色id')
    role_name = models.CharField(max_length=128, default='学生', verbose_name='角色身份')
    classes = models.SmallIntegerField(choices=class_choices, default=2, verbose_name='班级')
    age = models.SmallIntegerField(default=0, verbose_name='年龄')

    @property
    def class_name(self):
        return self.get_classes_display()

    class Meta:
        db_table = "students_info"
        verbose_name = "学生信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class SignDetail(models.Model):
    date_time = models.DateField(auto_now_add=True, verbose_name='日期')
    sign_number = models.SmallIntegerField(default=0, verbose_name='签到人数')
    no_sign_number = models.SmallIntegerField(default=0, verbose_name='未签到人数')

    class Meta:
        db_table = "sign_detail"
        verbose_name = "每日签到情况表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.date_time)


class Sign(models.Model):
    is_sign = models.BooleanField(default=False, verbose_name='是否签到')
    is_late = models.BooleanField(default=True, verbose_name='是否迟到')
    sign_time = models.DateTimeField(auto_now_add=True, verbose_name='签到时间')

    students = models.ForeignKey('Students', related_name='studentsign', on_delete=models.CASCADE, verbose_name="签到学生")
    sign_detail = models.ForeignKey('SignDetail', related_name='studentsigndetail', on_delete=models.DO_NOTHING, verbose_name="签到情况")

    class Meta:
        db_table = "sign"
        verbose_name = "学生签到表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.students.name


# class ErrorSubject(models.Model):
#     pass

# 学生试卷表
class TestPaper(models.Model):
    commit_time = models.DateTimeField(auto_now_add=True, null=True, verbose_name='提交时间')
    answer = models.TextField(verbose_name='答题内容')  # 暂时解决题目和答题内容对应,提交时前面加上试题id
    is_check = models.BooleanField(default=False, verbose_name='是否批改')

    students = models.ForeignKey('Students', on_delete=models.CASCADE, verbose_name='考生')
    test_bank = models.ForeignKey(te_models.TestBank, on_delete=models.DO_NOTHING, verbose_name='样卷')

    class Meta:
        db_table = "test_paper"
        verbose_name = "学生考卷表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.students.name + self.test_bank.title

    def students_name(self):
        return self.students.name

    def test_bank_name(self):
        return self.test_bank.title

    # 出题和阅卷老师名字
    def teachers_name(self):
        return self.test_bank.teachers.name

    def subjects_list(self):
        return self.test_bank.subjects_list()

    def source(self):
        try:
            res = self.grade.source
        except Exception:
            res = 0
        return res

    def test_bank_is_end(self):
        return self.test_bank.is_end

    def subjects_num(self):
        return len(self.subjects_list())


# 学生试卷成绩表，和试卷表一对一
class Grade(models.Model):
    source = models.SmallIntegerField(default=0, verbose_name='成绩')

    test_paper = models.OneToOneField('TestPaper', on_delete=models.CASCADE, verbose_name='考卷')

    class Meta:
        db_table = "grade"
        verbose_name = "学生成绩表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.test_paper.students.name + self.test_paper.test_bank.title + str(self.source)
