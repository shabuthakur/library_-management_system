from django.urls import path
from userrole.views import *
from django.contrib.auth import views
# from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('<slug:slug>/login/',LoginView.as_view()),

]