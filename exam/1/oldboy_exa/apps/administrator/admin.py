from django.contrib import admin
from . import models
# Register your models here.

class AdminsAdmin(admin.ModelAdmin):
    readonly_fields = ('create_time',)

admin.site.register(models.Admins, AdminsAdmin)