from django.db import models


class BaseModel(models.Model):
    #   name   username   password   sex      mobile     portrait   email     create_time       status
    sex_choices = (
        (0, '男'),
        (1, '女'),
        (2, '保密'),
    )
    name = models.CharField(max_length=128, verbose_name='姓名')
    sex = models.SmallIntegerField(choices=sex_choices, default=2, verbose_name='性别')
    username = models.CharField(max_length=128, verbose_name='账户', unique=True)
    password = models.CharField(max_length=128, verbose_name='密码')
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    portrait = models.ImageField(upload_to='icon', default='icon/default.png', verbose_name='头像')
    email = models.EmailField(max_length=256, verbose_name='邮箱')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    status = models.BooleanField(default=True, verbose_name='是否在校')

    class Meta:
        abstract = True
