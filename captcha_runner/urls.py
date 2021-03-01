"""captcha_runner/urls.py"""
from django.urls import path
from .import views

urlpatterns = [
    path('captcha', views.home, name='captcha'),
]
