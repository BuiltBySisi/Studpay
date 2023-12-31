from django.urls import re_path
from api import views

urlpatterns = [
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('token', views.tokenTest),
    re_path('logon', views.Login.as_view()),
    re_path('logout', views.Logout.as_view()),
    re_path('signon', views.Register.as_view()),
    re_path('studentsignup', views.studentSignup),
    re_path('usercheck', views.CredentialChecker.as_view()),
]
