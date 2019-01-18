from django.contrib import admin
from django.urls import re_path,include

from login import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^index/', views.index),
    re_path(r'^login/', views.login),
    re_path(r'^register/', views.register),
    re_path(r'^logout/', views.logout),
    re_path(r'^upload_file/',views.file_upload),
    re_path(r'^captcha', include('captcha.urls')),
]
