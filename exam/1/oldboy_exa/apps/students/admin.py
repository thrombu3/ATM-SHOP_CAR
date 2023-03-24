from django.contrib import admin
from . import models

# Register your models here.

# 指定的任何字段都将添加到可编辑字段之后。要控制顺序，可以使用fields选项。
# 显示情况下，在django admin后台，具有自动更新的日期字段，是不会显示在后台的。
# readonly_fields的配置是关键，因为自动日期具有不可编辑的内在属性。
class SignAdmin(admin.ModelAdmin):
    readonly_fields = ('sign_time',)

class TestPaperAdmin(admin.ModelAdmin):
    readonly_fields = ('commit_time',)

class SignDetailAdmin(admin.ModelAdmin):
    readonly_fields = ('date_time',)

class StudentsAdmin(admin.ModelAdmin):
    readonly_fields = ('create_time',)

admin.site.register(models.Sign, SignAdmin)
admin.site.register(models.Students, StudentsAdmin)
admin.site.register(models.SignDetail, SignDetailAdmin)
admin.site.register(models.TestPaper, TestPaperAdmin)
admin.site.register(models.Grade)

