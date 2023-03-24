from django.db import models
from oldboy_exa.utils.models import BaseModel

# Create your models here.


class Admins(BaseModel):
    role_id = models.SmallIntegerField(default=0,verbose_name='角色id')
    role_name = models.CharField(max_length=128, default='管理员', verbose_name='角色身份')

    class Meta:
        db_table = "admins_info"
        verbose_name = "管理员信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name








