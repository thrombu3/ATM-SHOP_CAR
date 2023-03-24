"""oldboy_exa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.routers import SimpleRouter
from teachers import views

router = SimpleRouter()
router.register('test-bank', views.TestBankView, 'test-bank')
router.register('subjects', views.SubjectsView, 'subjects')
router.register('teachers-paper', views.TeachersTestPaperView, 'teachers-paper')
router.register('teachers-edit-paper', views.TeachersEditPaperView, 'teachers-edit-paper')
router.register('', views.TeacherCommonView, 'teachers-common')
# 测试使用
router.register('', views.TestView, 'test-api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
