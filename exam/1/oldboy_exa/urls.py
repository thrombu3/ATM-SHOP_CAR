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
from django.urls import path, include
from oldboy_exa.common import views
from oldboy_exa.common import translation
from oldboy_exa.common import face_recogenition
from oldboy_exa.common import minio_files


urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('administrator/', include('administrator.urls')),
    path('login/', views.LoginViews.as_view()),
    path('verify_login/', views.VerifyLoginViews.as_view()),
    path('translation/', translation.TranslationViews.as_view()),
    path('face_compare/', face_recogenition.FaceCompareView.as_view()),
    path('change_password/', views.ChangePasswordView.as_view()),
    path('get_code/', views.SendCodeView.as_view()),
    path('check_password/', views.CheckOldPassView.as_view()),
    path('upload/', minio_files.MinIOFilesView.as_view()),
]
