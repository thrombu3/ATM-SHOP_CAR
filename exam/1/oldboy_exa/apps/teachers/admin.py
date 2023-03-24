from django.contrib import admin
from . import models
# Register your models here.


class TestBankAdmin(admin.ModelAdmin):
    readonly_fields = ('date_time',)

class TeachersAdmin(admin.ModelAdmin):
    readonly_fields = ('create_time',)


admin.site.register(models.Teachers, TeachersAdmin)
admin.site.register(models.Subjects)
admin.site.register(models.TestBank, TestBankAdmin)