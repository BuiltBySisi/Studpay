from django.urls import re_path
from api import views

urlpatterns = [
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('token', views.tokenTest),
]
