"""captcha_runner/views.py"""

# Django modules
from django.shortcuts import render

# My modules
from .my_captcha import FormWithCaptcha

def home(request):
    context = {
        'captcha': FormWithCaptcha,
    }
    return render(request, 'home.html', context)