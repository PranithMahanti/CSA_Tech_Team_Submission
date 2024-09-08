from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("signup/", authView, name="authView"),
    path("login/", loginPage, name="loginPage"),
    path("logout/", logoutUser, name="logoutUser"),
    path("user/", userPage, name="userPage"),
    path("done/<str:primary_key>/", done, name="done"),
    path("delete/<str:primary_key>/", deleteBookmark, name="deleteBookmark")
]
